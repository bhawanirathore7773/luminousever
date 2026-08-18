from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags

from apps.core.utils import generate_webp_content
from apps.core.validators import validate_image_file_size


class BlogCategory(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Blog categories"
        ordering = ["order"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Insights article (/insights/<slug>/). `content` accepts trusted HTML
    from Django Admin (no rich-text editor installed yet — plain <p>/<h2>
    tags work fine); `reading_time` auto-calculates from word count on save
    if left blank."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="blog_posts")

    excerpt = models.CharField(max_length=300)
    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True, validators=[validate_image_file_size])
    featured_image_webp = models.ImageField(
        upload_to="blog/webp/", blank=True, null=True, editable=False,
        help_text="Auto-generated from featured_image — do not upload directly.",
    )
    content = models.TextField(help_text="HTML content (h2/h3/p tags). Rendered as-is — admin-trusted input only.")
    reading_time = models.PositiveIntegerField(blank=True, null=True, help_text="Minutes. Auto-calculated on save if left blank.")

    published_date = models.DateTimeField(default=timezone.now)

    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    og_image = models.ImageField(upload_to="blog/og/", blank=True, null=True, validators=[validate_image_file_size])

    is_published = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_date"]
        indexes = [
            models.Index(fields=["slug", "is_published"]),
            models.Index(fields=["category", "is_published"]),
            models.Index(fields=["published_date"]),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.reading_time:
            word_count = len(strip_tags(self.content).split())
            self.reading_time = max(1, round(word_count / 200))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})


@receiver(post_save, sender=BlogPost)
def create_blog_post_webp(sender, instance, **kwargs):
    """See apps/portfolio/models.py::create_case_study_webp — same pattern."""
    if instance.featured_image and not instance.featured_image_webp:
        result = generate_webp_content(instance.featured_image)
        if result:
            name, content = result
            path = instance.featured_image_webp.field.generate_filename(instance, name)
            saved_path = instance.featured_image_webp.storage.save(path, content)
            BlogPost.objects.filter(pk=instance.pk).update(featured_image_webp=saved_path)
