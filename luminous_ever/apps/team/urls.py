"""Phase 7: real TeamMember grid replaces the Phase 3 "coming soon" placeholder."""

from django.urls import path

from .views import TeamIndexView

app_name = "team"

urlpatterns = [
    path("team/", TeamIndexView.as_view(), name="index"),
]
