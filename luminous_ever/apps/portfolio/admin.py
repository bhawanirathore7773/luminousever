from django.contrib import admin

from .models import CaseStudy, CaseStudyImage


class CaseStudyImageInline(admin.TabularInline):
    model = CaseStudyImage
    extra = 1


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "client_name", "category", "industry", "is_published", "order", "created_at")
    list_filter = ("category", "industry", "is_published")
    list_editable = ("order",)
    search_fields = ("title", "client_name", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("services",)
    inlines = [CaseStudyImageInline]

    fieldsets = (
        (None, {"fields": ("title", "slug", "client_name", "industry", "services", "category", "short_description", "featured_image", "order", "is_published")}),
        ("Case study narrative", {"fields": ("challenge", "objective", "strategy", "solution", "results", "technologies")}),
        ("Client testimonial", {"fields": ("testimonial_quote", "testimonial_author", "testimonial_role")}),
        ("SEO", {"fields": ("meta_title", "meta_description")}),
    )
