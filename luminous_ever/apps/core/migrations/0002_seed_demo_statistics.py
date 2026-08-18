from django.db import migrations


def seed_statistics(apps, schema_editor):
    Statistic = apps.get_model("core", "Statistic")
    demo_stats = [
        {"label": "Projects Delivered", "value": "50+", "order": 1},
        {"label": "Industries Served", "value": "20+", "order": 2},
        {"label": "Client Satisfaction", "value": "95%", "order": 3},
        {"label": "Average Growth Potential", "value": "3X", "order": 4},
    ]
    for stat in demo_stats:
        Statistic.objects.get_or_create(label=stat["label"], defaults=stat)


def remove_statistics(apps, schema_editor):
    Statistic = apps.get_model("core", "Statistic")
    Statistic.objects.filter(
        label__in=[
            "Projects Delivered",
            "Industries Served",
            "Client Satisfaction",
            "Average Growth Potential",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_statistics, remove_statistics),
    ]
