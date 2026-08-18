from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "company", "project_type", "rating", "source", "is_published", "order")
    list_filter = ("source", "is_published", "rating")
    list_editable = ("order",)
    search_fields = ("client_name", "company", "quote")
