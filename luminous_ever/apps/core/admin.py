from django.contrib import admin

from .models import SiteSettings, Statistic


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Singleton admin — always edits the same row, never lists/adds/deletes."""

    fieldsets = (
        ("Brand", {"fields": ("site_name", "tagline", "logo", "favicon")}),
        ("About page", {"fields": ("mission_statement", "vision_statement")}),
        ("Contact", {"fields": ("contact_email", "contact_phone", "whatsapp_number", "address", "business_hours")}),
        ("Social", {"fields": ("instagram_url", "facebook_url", "linkedin_url", "youtube_url")}),
        ("Default SEO", {"fields": ("default_meta_title", "default_meta_description", "default_og_image")}),
        ("Analytics", {"fields": ("google_analytics_id", "google_search_console_verification", "meta_pixel_id")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        from django.shortcuts import redirect
        return redirect("admin:core_sitesettings_change", obj.pk)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("order",)
