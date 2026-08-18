from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from .models import TeamMember


@method_decorator(cache_page(60 * 15), name="dispatch")
class TeamIndexView(TemplateView):
    """Phase 7: real /team/ grid, replacing the Phase 3 placeholder."""

    template_name = "team/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team_members"] = TeamMember.objects.filter(is_published=True)
        return context
