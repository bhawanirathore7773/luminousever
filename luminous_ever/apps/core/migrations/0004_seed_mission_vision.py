from django.db import migrations

MISSION = (
    "To give ambitious businesses the digital foundation, visibility and growth "
    "systems they need to get discovered, trusted and chosen — without having to "
    "manage five different vendors to get there."
)

VISION = (
    "A future where any serious business, regardless of size, has access to the "
    "same caliber of strategy, design and technology that only the biggest brands "
    "could once afford."
)


def seed(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    if not obj.mission_statement:
        obj.mission_statement = MISSION
    if not obj.vision_statement:
        obj.vision_statement = VISION
    obj.save()


def unseed(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    SiteSettings.objects.filter(pk=1).update(mission_statement="", vision_statement="")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_sitesettings_mission_statement_and_more"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
