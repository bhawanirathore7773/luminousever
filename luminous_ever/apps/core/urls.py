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
            template_name="core/legal_page.html",
            extra_context={
                "policy_key": "privacy",
                "policy_title": "Privacy Policy",
                "policy_description": "How Luminous Ever collects, uses, protects and retains personal information.",
            },
        ),
        name="privacy_policy",
    ),
    path(
        "terms/",
        TemplateView.as_view(
            template_name="core/legal_page.html",
            extra_context={
                "policy_key": "terms",
                "policy_title": "Terms & Conditions",
                "policy_description": "The rules governing use of the website and Luminous Ever's professional services.",
            },
        ),
        name="terms",
    ),
    path(
        "refund-policy/",
        TemplateView.as_view(
            template_name="core/legal_page.html",
            extra_context={
                "policy_key": "refund",
                "policy_title": "Refund Policy",
                "policy_description": "A clear framework for cancellations, recurring services, project work and refunds.",
            },
        ),
        name="refund_policy",
    ),
]
