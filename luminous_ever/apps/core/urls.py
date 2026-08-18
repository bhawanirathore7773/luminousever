from django.urls import path
from django.views.generic import TemplateView

from .views import AboutView, HomeView, StyleGuideView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("style-guide/", StyleGuideView.as_view(), name="style_guide"),
    path("about/", AboutView.as_view(), name="about"),
    path(
        "careers/",
        TemplateView.as_view(
            template_name="core/coming_soon.html",
            extra_context={"page_title": "Careers", "phase_note": "Coming soon"},
        ),
        name="careers",
    ),
    path(
        "privacy-policy/",
        TemplateView.as_view(
            template_name="core/coming_soon.html",
            extra_context={
                "page_title": "Privacy Policy",
                "phase_note": "Coming soon",
                "page_description": "Real policy text goes here once the business's data-handling specifics are finalized — not something to draft generically.",
            },
        ),
        name="privacy_policy",
    ),
    path(
        "terms/",
        TemplateView.as_view(
            template_name="core/coming_soon.html",
            extra_context={"page_title": "Terms of Service", "phase_note": "Coming soon"},
        ),
        name="terms",
    ),
    path(
        "refund-policy/",
        TemplateView.as_view(
            template_name="core/coming_soon.html",
            extra_context={"page_title": "Refund Policy", "phase_note": "Coming soon"},
        ),
        name="refund_policy",
    ),
]
