from django.db.models import Prefetch
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, TemplateView

from apps.core.schema import breadcrumb_list_schema, service_schema

from .models import Industry, Service, ServiceCategory


@method_decorator(cache_page(60 * 15), name="dispatch")
class SAPConsultingView(TemplateView):
    """Legacy route kept only as a clean bridge to the separate SAP site."""

    def get(self, request, *args, **kwargs):
        return redirect("https://luminousever.consulting/")


@method_decorator(cache_page(60 * 15), name="dispatch")
class ServiceIndexView(TemplateView):
    """The /services/ hub — categories with their services, matching the
    #build #grow #brand #optimize anchors already linked from the navbar
    and homepage."""

    template_name = "services/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = (
            ServiceCategory.objects
            .exclude(slug="sap-consulting")
            .prefetch_related(
                Prefetch("services", queryset=Service.objects.filter(is_published=True))
            )
            .order_by("order")
        )
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/detail.html"
    context_object_name = "service"

    def dispatch(self, request, *args, **kwargs):
        if str(kwargs.get("slug", "")).startswith("sap-"):
            return redirect("https://luminousever.consulting/")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Service.objects.filter(is_published=True)
            .select_related("category")
            .prefetch_related("case_studies")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_services"] = self.object.related_services()
        context["service_schema_json"] = service_schema(self.object, self.request)
        context["breadcrumb_schema_json"] = breadcrumb_list_schema([
            ("Home", self.request.build_absolute_uri(reverse("core:home"))),
            ("Services", self.request.build_absolute_uri(reverse("services:index"))),
            (self.object.name, None),
        ])
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class IndustryIndexView(TemplateView):
    template_name = "industries/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["industries"] = Industry.objects.filter(is_published=True).order_by("order")
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class IndustryDetailView(DetailView):
    model = Industry
    template_name = "industries/detail.html"
    context_object_name = "industry"

    def get_queryset(self):
        return Industry.objects.filter(is_published=True).prefetch_related("relevant_services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb_schema_json"] = breadcrumb_list_schema([
            ("Home", self.request.build_absolute_uri(reverse("core:home"))),
            ("Industries", self.request.build_absolute_uri(reverse("services:industries"))),
            (self.object.name, None),
        ])
        return context
