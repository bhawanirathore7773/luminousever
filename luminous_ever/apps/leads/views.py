from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from .forms import LeadForm

RATE_LIMIT_MAX_ATTEMPTS = 5
RATE_LIMIT_WINDOW_SECONDS = 60 * 60  # 1 hour


class ContactView(FormView):
    """
    Phase 9: the real /contact/ page, replacing the Phase 3 placeholder.
    UTM/landing-page attribution is pulled from the session — captured by
    UTMTrackingMiddleware (apps/core/middleware.py, Phase 1) on first visit,
    not resubmitted by the visitor.

    Phase 12: rate-limited per IP (5 submissions/hour) on top of the
    existing honeypot — every POST counts toward the limit regardless of
    whether it ultimately validates, so repeated invalid submissions can't
    be used to route around it. Uses the cache framework from Phase 11,
    so this works with either the local dev cache or Redis in production
    with no extra setup.
    """

    template_name = "leads/contact.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:contact") + "?submitted=1"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submitted"] = self.request.GET.get("submitted") == "1"
        return context

    def post(self, request, *args, **kwargs):
        if self._is_rate_limited(request):
            return render(
                request,
                self.template_name,
                self.get_context_data(form=self.get_form(), rate_limited=True),
                status=429,
            )
        self._record_attempt(request)
        return super().post(request, *args, **kwargs)

    def _rate_limit_cache_key(self, request):
        ip = request.META.get("REMOTE_ADDR", "unknown")
        return f"contact-form-attempts:{ip}"

    def _is_rate_limited(self, request):
        return cache.get(self._rate_limit_cache_key(request), 0) >= RATE_LIMIT_MAX_ATTEMPTS

    def _record_attempt(self, request):
        key = self._rate_limit_cache_key(request)
        try:
            cache.incr(key)
        except ValueError:
            cache.set(key, 1, RATE_LIMIT_WINDOW_SECONDS)

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.utm_source = self.request.session.get("utm_source", "")
        lead.utm_medium = self.request.session.get("utm_medium", "")
        lead.utm_campaign = self.request.session.get("utm_campaign", "")
        lead.landing_page = self.request.session.get("landing_page", "")
        lead.save()
        form.save_m2m()

        self._send_notification_email(lead)
        return super().form_valid(form)

    def _send_notification_email(self, lead):
        subject = f"New lead: {lead.name}" + (f" ({lead.business_name})" if lead.business_name else "")
        body_lines = [
            f"Name: {lead.name}",
            f"Business: {lead.business_name or '-'}",
            f"Phone: {lead.phone}",
            f"Email: {lead.email}",
            f"Website: {lead.website or '-'}",
            f"Business type: {lead.business_type or '-'}",
            f"Budget: {lead.get_budget_range_display() if lead.budget_range else '-'}",
            f"Services: {', '.join(s.name for s in lead.services_required.all()) or '-'}",
            f"Message: {lead.message or '-'}",
            "",
            f"Source: {lead.lead_source}",
            f"UTM: {lead.utm_source or '-'} / {lead.utm_medium or '-'} / {lead.utm_campaign or '-'}",
            f"Landing page: {lead.landing_page or '-'}",
        ]
        try:
            send_mail(
                subject=subject,
                message="\n".join(body_lines),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.LEAD_NOTIFICATION_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass  # a failed notification email should never block lead capture
