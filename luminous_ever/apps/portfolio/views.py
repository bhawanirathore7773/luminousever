from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, TemplateView

from apps.core.schema import breadcrumb_list_schema

from .models import CaseStudy


@method_decorator(cache_page(60 * 15), name="dispatch")
class PortfolioIndexView(TemplateView):
    """The /work/ grid — filterable client-side by category (data-filter
    buttons + JS), so no separate URL/view is needed per category."""

    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["case_studies"] = (
            CaseStudy.objects.filter(is_published=True)
            .select_related("industry")
        )
        context["categories"] = CaseStudy.CATEGORY_CHOICES
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class CaseStudyDetailView(DetailView):
    model = CaseStudy
    template_name = "portfolio/detail.html"
    context_object_name = "case_study"

    def get_queryset(self):
        return CaseStudy.objects.filter(is_published=True).select_related("industry").prefetch_related(
            "services", "gallery"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_case_studies"] = (
            CaseStudy.objects.filter(is_published=True, category=self.object.category)
            .exclude(pk=self.object.pk)[:3]
        )
        context["breadcrumb_schema_json"] = breadcrumb_list_schema([
            ("Home", self.request.build_absolute_uri(reverse("core:home"))),
            ("Work", self.request.build_absolute_uri(reverse("portfolio:index"))),
            (self.object.title, None),
        ])
        return context
