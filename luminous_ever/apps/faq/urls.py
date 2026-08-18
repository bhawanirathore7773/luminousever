"""Phase 8: real FAQ list replaces the Phase 3 "coming soon" placeholder."""

from django.urls import path

from .views import FAQIndexView

app_name = "faq"

urlpatterns = [
    path("faq/", FAQIndexView.as_view(), name="index"),
]
