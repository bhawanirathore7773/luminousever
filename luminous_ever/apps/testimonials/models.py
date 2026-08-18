from django.db import models

from apps.core.validators import validate_image_file_size


class Testimonial(models.Model):
    """
    Standalone client testimonial (homepage grid, etc.) — distinct from
    the per-project testimonial fields already on CaseStudy. `source` and
    `google_review_url` exist now so Google Review sync can be added later
    (per the brief) without a schema change.
    """

    SOURCE_CHOICES = [
        ("direct", "Direct / Manual"),
        ("google", "Google Review"),
    ]

    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=150, blank=True)
    designation = models.CharField(max_length=150, blank=True)
    quote = models.TextField()
    project_type = models.CharField(max_length=100, blank=True, help_text="e.g. 'Website & Branding'")
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True, validators=[validate_image_file_size])

    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default="direct")
    google_review_url = models.URLField(blank=True, help_text="Reserved for future Google Review integration.")
    rating = models.PositiveSmallIntegerField(default=5, help_text="1–5 stars")

    is_published = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.client_name} — {self.company or 'N/A'}"

    @property
    def initials(self):
        parts = self.client_name.split()
        return "".join(p[0] for p in parts[:2]).upper()
