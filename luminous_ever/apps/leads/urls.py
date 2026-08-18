"""Phase 9: the real contact form + lead capture replaces the Phase 3 placeholder."""

from django.urls import path

from .views import ContactView

app_name = "leads"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
]
