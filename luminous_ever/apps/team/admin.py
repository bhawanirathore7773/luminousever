from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_published", "order")
    list_filter = ("is_published",)
    list_editable = ("order",)
    search_fields = ("name", "role")
