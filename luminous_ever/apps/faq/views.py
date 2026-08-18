from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from .models import FAQ


@method_decorator(cache_page(60 * 15), name="dispatch")
class FAQIndexView(TemplateView):
    """Phase 8: real /faq/ page with all published questions and FAQPage
    JSON-LD schema, replacing the Phase 3 placeholder."""

    template_name = "faq/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["faqs"] = FAQ.objects.filter(is_published=True)
        return context
