"""Phase 8: real BlogPost index/detail views replace the Phase 3 placeholder."""

from django.urls import path

from .views import BlogDetailView, BlogIndexView

app_name = "blog"

urlpatterns = [
    path("insights/", BlogIndexView.as_view(), name="index"),
    path("insights/<slug:slug>/", BlogDetailView.as_view(), name="detail"),
]
