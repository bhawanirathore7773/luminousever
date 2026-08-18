from django.db import models

from apps.core.validators import validate_image_file_size


class TeamMember(models.Model):
    """Premium team card — /team/ grid. Photo is optional; the template
    falls back to an initials avatar when none is uploaded."""

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/", blank=True, null=True, validators=[validate_image_file_size])
    bio = models.TextField()
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    skills = models.JSONField(default=list, blank=True, help_text="List of skill strings.")

    is_published = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} — {self.role}"

    @property
    def initials(self):
        parts = self.name.split()
        return "".join(p[0] for p in parts[:2]).upper()
