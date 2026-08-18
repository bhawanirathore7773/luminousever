"""Phase 6: real CaseStudy views replace the Phase 3 "coming soon" placeholder."""

from django.urls import path

from .views import CaseStudyDetailView, PortfolioIndexView

app_name = "portfolio"

urlpatterns = [
    path("work/", PortfolioIndexView.as_view(), name="index"),
    path("work/<slug:slug>/", CaseStudyDetailView.as_view(), name="detail"),
]
