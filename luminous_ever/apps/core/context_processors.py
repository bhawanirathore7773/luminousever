from django.db.utils import OperationalError, ProgrammingError

from .models import SiteSettings
from .schema import safe_json_dumps


def site_settings(request):
    """
    Makes SiteSettings available in every template as `{{ site_settings }}`,
    and builds the sitewide Organization/ProfessionalService + WebSite
    JSON-LD from the same instance (avoids querying SiteSettings twice per
    request across two separate context processors — Phase 11 caught this).
    Fails gracefully before the first migration/deploy has run.
    """
    try:
        settings_obj = SiteSettings.load()
    except (OperationalError, ProgrammingError):
        return {"site_settings": None, "sitewide_schema_json": ""}

    return {
        "site_settings": settings_obj,
        "sitewide_schema_json": _build_sitewide_schema(settings_obj, request),
    }


def _build_sitewide_schema(settings_obj, request):
    """
    Organization/ProfessionalService + WebSite JSON-LD, rendered once in
    base.html on every page. Built as a Python dict and serialized with
    json.dumps — hand-assembling JSON-LD in a template with conditional
    fields is a trailing-comma bug waiting to happen.

    Uses ProfessionalService (not plain Organization) since that's what
    the business actually is, and it's valid schema.org whether or not a
    physical address is set. Address is only included if one is — no
    fabricated location, per the brief.
    """
    base_url = request.build_absolute_uri("/").rstrip("/")
    site_name = settings_obj.site_name or "Luminous Ever"

    organization = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": site_name,
        "url": base_url,
    }
    if settings_obj.tagline:
        organization["description"] = settings_obj.tagline
    if settings_obj.logo:
        organization["logo"] = request.build_absolute_uri(settings_obj.logo.url)
    if settings_obj.contact_email:
        organization["email"] = settings_obj.contact_email
    if settings_obj.contact_phone:
        organization["telephone"] = settings_obj.contact_phone
    if settings_obj.address:
        organization["address"] = {"@type": "PostalAddress", "streetAddress": settings_obj.address}

    same_as = [
        url for url in [
            settings_obj.instagram_url, settings_obj.facebook_url,
            settings_obj.linkedin_url, settings_obj.youtube_url,
        ] if url
    ]
    if same_as:
        organization["sameAs"] = same_as

    website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": site_name,
        "url": base_url,
    }

    return safe_json_dumps([organization, website])
