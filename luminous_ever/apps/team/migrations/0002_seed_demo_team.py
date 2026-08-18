from django.db import migrations

TEAM_MEMBERS = [
    {
        "name": "Aarav Mehta", "role": "Founder & Digital Strategist", "order": 1,
        "bio": "Leads strategy and client partnerships, translating business goals into a digital roadmap that actually gets executed.",
        "skills": ["Strategy", "Business Development", "Client Partnerships"],
    },
    {
        "name": "Priya Nair", "role": "UI/UX Designer", "order": 2,
        "bio": "Designs interfaces that are as functional as they are premium, with a close eye on the details most people never consciously notice.",
        "skills": ["UI Design", "UX Research", "Figma", "Design Systems"],
    },
    {
        "name": "Rohan Verma", "role": "Full Stack Developer", "order": 3,
        "bio": "Builds the Django backbone behind every site — fast, secure, and built to scale without needing a rewrite a year later.",
        "skills": ["Django", "Python", "PostgreSQL", "REST APIs"],
    },
    {
        "name": "Ananya Iyer", "role": "SEO Specialist", "order": 4,
        "bio": "Digs into technical SEO and content strategy to get clients found by people who are already looking for them.",
        "skills": ["Technical SEO", "Content Strategy", "Google Search Console"],
    },
    {
        "name": "Kabir Singh", "role": "Performance Marketer", "order": 5,
        "bio": "Runs Google and Meta Ads campaigns with a relentless focus on cost per lead, not just clicks.",
        "skills": ["Google Ads", "Meta Ads", "Conversion Tracking"],
    },
    {
        "name": "Diya Kapoor", "role": "Social Media Manager", "order": 6,
        "bio": "Keeps every client's social presence consistent, on-brand, and actually posting on schedule.",
        "skills": ["Content Calendars", "Community Management", "Instagram Strategy"],
    },
    {
        "name": "Vikram Rao", "role": "Graphic Designer", "order": 7,
        "bio": "Builds the visual identity systems and creative assets that keep every brand touchpoint consistent.",
        "skills": ["Branding", "Adobe Creative Suite", "Print & Digital Design"],
    },
    {
        "name": "Meera Joshi", "role": "Content Creator", "order": 8,
        "bio": "Writes and produces content that actually sounds like the brand it represents, not generic marketing copy.",
        "skills": ["Copywriting", "Content Production", "Video & Reels"],
    },
]


def seed(apps, schema_editor):
    TeamMember = apps.get_model("team", "TeamMember")
    for member in TEAM_MEMBERS:
        TeamMember.objects.get_or_create(name=member["name"], defaults=member)


def unseed(apps, schema_editor):
    TeamMember = apps.get_model("team", "TeamMember")
    TeamMember.objects.filter(name__in=[m["name"] for m in TEAM_MEMBERS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
