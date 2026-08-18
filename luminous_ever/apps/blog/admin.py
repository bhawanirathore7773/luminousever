from django.contrib import admin

from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "published_date", "reading_time", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"

    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "author", "featured_image", "is_published")}),
        ("Content", {"fields": ("excerpt", "content", "reading_time", "published_date")}),
        ("SEO", {"fields": ("meta_title", "meta_description", "og_image")}),
    )
