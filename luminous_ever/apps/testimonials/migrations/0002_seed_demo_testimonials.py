from django.db import migrations

TESTIMONIALS = [
    {
        "client_name": "R. Mehta", "company": "Demo Retail Co.", "designation": "Founder", "order": 1,
        "quote": "Our new site finally looks like the business we actually are — leads started coming in within the first month.",
        "project_type": "Website & SEO",
    },
    {
        "client_name": "S. Kapoor", "company": "Demo Manufacturing Co.", "designation": "Marketing Head", "order": 2,
        "quote": "They didn't just build a website. They gave us a growth system we actually understand.",
        "project_type": "Website & Strategy",
    },
    {
        "client_name": "A. Iyer", "company": "Demo Hospitality Co.", "designation": "Owner", "order": 3,
        "quote": "Clear reporting, real strategy, and a team that actually explains what they're doing and why.",
        "project_type": "Social Media & Branding",
    },
    {
        "client_name": "N. Sharma", "company": "Demo Beauty Brand", "designation": "Marketing Manager", "order": 4,
        "quote": "Response times are fast and every deliverable actually matches what we asked for — no surprises.",
        "project_type": "E-commerce",
    },
    {
        "client_name": "J. Thomas", "company": "Demo B2B Services Co.", "designation": "CEO", "order": 5,
        "quote": "We've worked with agencies before — this is the first one that felt like a real partner instead of a vendor.",
        "project_type": "Website & Automation",
    },
]


def seed(apps, schema_editor):
    Testimonial = apps.get_model("testimonials", "Testimonial")
    for t in TESTIMONIALS:
        Testimonial.objects.get_or_create(client_name=t["client_name"], company=t["company"], defaults=t)


def unseed(apps, schema_editor):
    Testimonial = apps.get_model("testimonials", "Testimonial")
    Testimonial.objects.filter(client_name__in=[t["client_name"] for t in TESTIMONIALS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("testimonials", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
