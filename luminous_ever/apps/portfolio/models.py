from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from apps.core.utils import generate_webp_content
from apps.core.validators import validate_image_file_size

from apps.services.models import Industry, Service


class CaseStudy(models.Model):
    """
    A portfolio project with its own detail page (/work/<slug>/). Doubles
    as the "Project" grid card (short_description, featured_image,
    category) and the full "CaseStudy" narrative (challenge, objective,
    strategy, solution, results) — the brief's own field list treats these
    as one model rather than two, so that's how this is built.
    """

    CATEGORY_CHOICES = [
        ("websites", "Websites"),
        ("ecommerce", "E-commerce"),
        ("branding", "Branding"),
        ("social-media", "Social Media"),
        ("seo", "SEO"),
        ("ads", "Ads"),
        ("creative", "Creative"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    client_name = models.CharField(max_length=150, help_text="e.g. 'Demo Fashion Brand' — clearly marked as demo until real clients are added.")
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True, related_name="case_studies")
    services = models.ManyToManyField(Service, blank=True, related_name="case_studies")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)

    short_description = models.CharField(max_length=200, help_text="Shown on grid cards.")
    challenge = models.TextField()
    objective = models.TextField()
    strategy = models.TextField()
    solution = models.TextField(help_text="What was actually built/delivered.")
    results = models.TextField()
    technologies = models.JSONField(default=list, blank=True)

    featured_image = models.ImageField(upload_to="portfolio/", blank=True, null=True, validators=[validate_image_file_size])
    featured_image_webp = models.ImageField(
        upload_to="portfolio/webp/", blank=True, null=True, editable=False,
        help_text="Auto-generated from featured_image — do not upload directly.",
    )

    testimonial_quote = models.TextField(blank=True)
    testimonial_author = models.CharField(max_length=100, blank=True)
    testimonial_role = models.CharField(max_length=150, blank=True)

    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    is_published = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Case studies"
        ordering = ["order", "-created_at"]
        indexes = [
            models.Index(fields=["slug", "is_published"]),
            models.Index(fields=["category", "is_published"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:detail", kwargs={"slug": self.slug})

    @property
    def has_testimonial(self):
        return bool(self.testimonial_quote)


class CaseStudyImage(models.Model):
    """Gallery images for a case study. Empty for demo data — real photos
    get added from Django Admin as projects are delivered."""

    case_study = models.ForeignKey(CaseStudy, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="portfolio/gallery/", validators=[validate_image_file_size])
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.case_study.title} — image {self.order}"


@receiver(post_save, sender=CaseStudy)
def create_case_study_webp(sender, instance, **kwargs):
    """
    Generates a WebP companion for featured_image on first save. Only
    fires when featured_image_webp is empty — if an admin later swaps the
    image, clearing featured_image_webp first will trigger regeneration.
    Uses queryset.update() (not instance.save()) to avoid re-triggering
    this same signal.
    """
    if instance.featured_image and not instance.featured_image_webp:
        result = generate_webp_content(instance.featured_image)
        if result:
            name, content = result
            path = instance.featured_image_webp.field.generate_filename(instance, name)
            saved_path = instance.featured_image_webp.storage.save(path, content)
            CaseStudy.objects.filter(pk=instance.pk).update(featured_image_webp=saved_path)
