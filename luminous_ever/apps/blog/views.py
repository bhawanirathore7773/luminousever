from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, TemplateView

from apps.core.schema import breadcrumb_list_schema

from .models import BlogCategory, BlogPost


@method_decorator(cache_page(60 * 15), name="dispatch")
class BlogIndexView(TemplateView):
    """Phase 8: real /insights/ index, replacing the Phase 3 placeholder.
    Category filter tabs work the same way as the portfolio grid (Phase 6):
    client-side, no reload.

    Paginated (Phase 11) since a blog is the one listing page on this site
    that's genuinely unbounded and chronological — services/industries/
    portfolio are curated catalogs sized by what's published, not an
    ever-growing feed. Note: the client-side category filter only filters
    within the current page once there's more than one page; that's an
    accepted trade-off for keeping the filter instant/no-reload rather than
    round-tripping to the server per filter click.
    """

    template_name = "blog/index.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = (
            BlogPost.objects.filter(is_published=True)
            .select_related("category", "author")
        )
        paginator = Paginator(post_list, self.paginate_by)
        context["posts"] = paginator.get_page(self.request.GET.get("page"))
        context["categories"] = BlogCategory.objects.all()
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).select_related("category", "author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_posts"] = (
            BlogPost.objects.filter(is_published=True, category=self.object.category)
            .exclude(pk=self.object.pk)[:3]
        )
        context["breadcrumb_schema_json"] = breadcrumb_list_schema([
            ("Home", self.request.build_absolute_uri(reverse("core:home"))),
            ("Insights", self.request.build_absolute_uri(reverse("blog:index"))),
            (self.object.title, None),
        ])
        return context
