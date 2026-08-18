from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "business_name", "status", "budget_range", "lead_source", "created_at")
    list_filter = ("status", "budget_range", "lead_source", "utm_source")
    list_editable = ("status",)
    search_fields = ("name", "business_name", "email", "phone", "message")
    filter_horizontal = ("services_required",)
    date_hierarchy = "created_at"
    readonly_fields = ("lead_source", "utm_source", "utm_medium", "utm_campaign", "landing_page", "created_at", "updated_at")

    fieldsets = (
        ("Contact", {"fields": ("name", "business_name", "phone", "email", "website")}),
        ("Project", {"fields": ("business_type", "services_required", "budget_range", "message")}),
        ("Pipeline", {"fields": ("status",)}),
        ("Attribution", {"fields": ("lead_source", "utm_source", "utm_medium", "utm_campaign", "landing_page")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
