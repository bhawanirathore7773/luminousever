from django.conf import settings
from django.db import migrations


def update_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    domain = getattr(settings, "SITE_DOMAIN", "luminousever.com")
    site_name = getattr(settings, "SITE_NAME", "Luminous Ever")
    Site.objects.update_or_create(
        pk=1,
        defaults={"domain": domain, "name": site_name},
    )


def revert_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(pk=1).update(domain="example.com", name="example.com")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_seed_mission_vision"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(update_site, revert_site),
    ]
