from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from apps.blog.models import BlogPost
from apps.faq.models import FAQ
from apps.portfolio.models import CaseStudy
from apps.testimonials.models import Testimonial

from .models import Statistic

# Demo content still hardcoded for pieces without their own model:
# social content types are just labels for the homepage grid (no real
# social posts to pull from yet). Everything else now comes from the
# database (Statistic, CaseStudy, Testimonial, BlogPost, FAQ).
SOCIAL_CONTENT_TYPES = [
    "Reel", "Product Creative", "Campaign Graphic", "Educational Post",
    "Brand Post", "Testimonial Post", "Behind the Scenes", "Launch Announcement",
]

INDUSTRIES = [
    "Retail", "E-commerce", "Manufacturing", "Real Estate", "Healthcare",
    "Hospitality", "Professional Services", "Fashion", "Startups",
]


@method_decorator(cache_page(60 * 15), name="dispatch")
class HomeView(TemplateView):
    """Phase 4: the full homepage build."""

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statistics"] = Statistic.objects.filter(is_active=True)
        context["demo_projects"] = CaseStudy.objects.filter(is_published=True).select_related("industry")[:6]
        context["social_content_types"] = SOCIAL_CONTENT_TYPES
        context["industries"] = INDUSTRIES
        context["demo_testimonials"] = Testimonial.objects.filter(is_published=True)[:3]
        context["latest_posts"] = BlogPost.objects.filter(is_published=True).select_related("category")[:3]
        context["faqs"] = FAQ.objects.filter(is_published=True)[:6]
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class AboutView(TemplateView):
    """Phase 7: the real About page — mission/vision (from SiteSettings),
    values, and what we combine."""

    template_name = "about/index.html"


class StyleGuideView(TemplateView):
    """
    Phase 2 deliverable — internal-only preview of every design token and
    component (colors, type scale, buttons, cards, forms, motion). Not
    linked from the public site; noindex'd. Safe to keep around as a living
    reference for later phases, or remove once the real pages are built.
    """

    template_name = "dev/style-guide.html"


def robots_txt(request):
    """
    Plain-text robots.txt, built as a view (not a static file) so the
    Sitemap line always points at the real domain instead of needing to
    stay in sync manually.
    """
    domain = request.build_absolute_uri("/").rstrip("/")
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Disallow: /{settings.ADMIN_URL_PATH}",
        "Disallow: /style-guide/",
        "",
        f"Sitemap: {domain}{reverse('django.contrib.sitemaps.views.sitemap')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
