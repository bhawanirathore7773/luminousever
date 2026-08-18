from django.db import models
from django.urls import reverse


class ServiceCategory(models.Model):
    """The 4 pillars: Build, Grow, Brand, Optimize."""

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    tagline = models.CharField(max_length=120, help_text="e.g. 'Digital foundations'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Service categories"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    One major service with its own detail page
    (/services/<slug>/) — Hero, Problem, Solution, Features, Technology,
    Benefits, Who it's for, Deliverables and FAQ all live here so the whole
    page is editable from Django Admin without touching code.
    """

    category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, related_name="services")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    short_description = models.CharField(max_length=200, help_text="Shown on service cards and index pages.")

    hero_subtitle = models.TextField(help_text="1–2 sentence hero subheading for the detail page.")
    problem = models.TextField(help_text="The problem this service solves.")
    solution = models.TextField(help_text="How Luminous Ever solves it.")

    # Each a JSON list — flexible, admin-editable, no extra tables needed
    # for what is fundamentally page copy.
    features = models.JSONField(
        default=list, blank=True,
        help_text='List of {"title": "...", "description": "..."} objects.',
    )
    technologies = models.JSONField(default=list, blank=True, help_text="List of technology/tool names.")
    benefits = models.JSONField(default=list, blank=True, help_text="List of benefit strings.")
    who_its_for = models.JSONField(default=list, blank=True, help_text="List of audience descriptions.")
    deliverables = models.JSONField(default=list, blank=True, help_text="List of deliverable strings.")
    faqs = models.JSONField(
        default=list, blank=True,
        help_text='List of {"question": "...", "answer": "..."} objects.',
    )

    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    is_published = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category__order", "order"]
        indexes = [
            models.Index(fields=["slug", "is_published"]),
            models.Index(fields=["category", "is_published"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})

    def related_services(self, count=3):
        return (
            Service.objects.filter(category=self.category, is_published=True)
            .exclude(pk=self.pk)[:count]
        )


class Industry(models.Model):
    """
    Industry-specific landing page (/industries/<slug>/). Lighter than a
    Service page by design — it explains the industry's challenges and
    points at the existing, already-detailed services that address them,
    rather than duplicating full service content per industry.
    """

    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True, db_index=True)
    description = models.TextField(help_text="1–2 paragraph intro specific to this industry.")
    challenges = models.JSONField(default=list, blank=True, help_text="List of industry-specific challenge strings.")
    relevant_services = models.ManyToManyField(Service, blank=True, related_name="industries")

    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    is_published = models.BooleanField(default=True, db_index=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Industries"
        ordering = ["order"]
        indexes = [models.Index(fields=["slug", "is_published"])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("services:industry_detail", kwargs={"slug": self.slug})
