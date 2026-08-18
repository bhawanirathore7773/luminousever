from django.db import models

from apps.core.validators import phone_validator


class Lead(models.Model):
    """
    A contact-form submission. Consolidates the brief's separate "Lead"
    and "ContactMessage" models — one field set covers both, and a single
    pipeline is simpler to actually manage from Django Admin.
    """

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("proposal_sent", "Proposal Sent"),
        ("won", "Won"),
        ("lost", "Lost"),
    ]

    BUDGET_CHOICES = [
        ("under_25k", "Under ₹25,000"),
        ("25k_50k", "₹25,000–₹50,000"),
        ("50k_1l", "₹50,000–₹1,00,000"),
        ("1l_plus", "₹1,00,000+"),
        ("not_sure", "Not Sure"),
    ]

    # ---- Form fields ----
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    email = models.EmailField()
    website = models.URLField(blank=True)
    business_type = models.CharField(max_length=100, blank=True)
    services_required = models.ManyToManyField("services.Service", blank=True, related_name="leads")
    budget_range = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True)
    message = models.TextField(blank=True)

    # ---- Pipeline ----
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new", db_index=True)

    # ---- Attribution (lead_source/UTM/landing_page populate from the
    # UTMTrackingMiddleware session data set in Phase 1 — not user input) ----
    lead_source = models.CharField(max_length=100, blank=True, default="Contact Form")
    utm_source = models.CharField(max_length=100, blank=True)
    utm_medium = models.CharField(max_length=100, blank=True)
    utm_campaign = models.CharField(max_length=100, blank=True)
    landing_page = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "created_at"]),
        ]

    def __str__(self):
        return f"{self.name} — {self.business_name or 'N/A'} ({self.get_status_display()})"
