from django.contrib import admin

from .models import Industry, Service, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_published", "order", "updated_at")
    list_filter = ("category", "is_published")
    list_editable = ("order",)
    search_fields = ("name", "short_description")
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        (None, {"fields": ("category", "name", "slug", "short_description", "order", "is_published")}),
        ("Detail page content", {"fields": ("hero_subtitle", "problem", "solution")}),
        ("Structured content (JSON)", {
            "fields": ("features", "technologies", "benefits", "who_its_for", "deliverables", "faqs"),
            "description": (
                "features/faqs are lists of objects, e.g. "
                '[{"title": "...", "description": "..."}]. '
                "technologies/benefits/who_its_for/deliverables are plain string lists."
            ),
        }),
        ("SEO", {"fields": ("meta_title", "meta_description")}),
    )


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_published", "order")
    list_filter = ("is_published",)
    list_editable = ("order",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("relevant_services",)
