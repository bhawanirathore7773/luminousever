from django.db import models

from apps.core.validators import validate_image_file_size


class SiteSettings(models.Model):
    """
    Singleton model holding global, non-code-change site configuration.
    Editable from Django Admin — powers footer, header CTAs, schema.org data
    and analytics IDs across every template.
    """

    site_name = models.CharField(max_length=100, default="Luminous Ever")
    tagline = models.CharField(
        max_length=200,
        blank=True,
        help_text="Short positioning line, e.g. shown near the logo or in meta tags.",
    )
    mission_statement = models.TextField(blank=True, help_text="Shown on the About page.")
    vision_statement = models.TextField(blank=True, help_text="Shown on the About page.")
    logo = models.ImageField(upload_to="site/", blank=True, null=True, validators=[validate_image_file_size])
    favicon = models.ImageField(upload_to="site/", blank=True, null=True, validators=[validate_image_file_size])

    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    whatsapp_number = models.CharField(
        max_length=20, blank=True, help_text="Digits only, with country code, e.g. 91XXXXXXXXXX"
    )
    address = models.TextField(blank=True)
    business_hours = models.CharField(max_length=200, blank=True)

    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    default_meta_title = models.CharField(max_length=70, blank=True)
    default_meta_description = models.CharField(max_length=160, blank=True)
    default_og_image = models.ImageField(upload_to="site/", blank=True, null=True, validators=[validate_image_file_size])

    google_analytics_id = models.CharField(max_length=30, blank=True)
    google_search_console_verification = models.CharField(max_length=100, blank=True)
    meta_pixel_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # prevent deletion from Admin

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Statistic(models.Model):
    """Homepage 'Results / Numbers' entries, e.g. '50+ Projects Delivered'."""

    label = models.CharField(max_length=100, help_text="e.g. Projects Delivered")
    value = models.CharField(max_length=20, help_text="e.g. 50+, 95%, 3X")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} {self.label}"
