from django.db import migrations

FAQS = [
    {
        "question": "How much does a website cost?",
        "answer": "It depends on scope — a landing page and a full e-commerce platform aren't priced the same way. Tell us what you need on a discovery call and we'll give you a clear, tailored quote.",
        "order": 1,
    },
    {
        "question": "How long does a website take?",
        "answer": "Most business websites take a few weeks from kickoff to launch; larger platforms with custom features take longer. We'll give you a realistic timeline before any work starts.",
        "order": 2,
    },
    {
        "question": "Do you provide website maintenance?",
        "answer": "Yes — ongoing maintenance, security updates and support plans are available so the site keeps running smoothly after launch.",
        "order": 3,
    },
    {
        "question": "Do you manage social media?",
        "answer": "Yes — content planning, creative and posting across Instagram, Facebook and LinkedIn, either as a standalone service or part of a full package.",
        "order": 4,
    },
    {
        "question": "Do you run Google Ads?",
        "answer": "Yes — search, display and shopping campaigns, set up with conversion tracking from day one so performance is measurable, not a guess.",
        "order": 5,
    },
    {
        "question": "Do you run Meta Ads?",
        "answer": "Yes — Instagram and Facebook campaigns, including creative direction, audience targeting and retargeting.",
        "order": 6,
    },
    {
        "question": "Can you redesign an existing website?",
        "answer": "Yes — we regularly rebuild and modernize existing sites, migrating content and preserving SEO value along the way.",
        "order": 7,
    },
    {
        "question": "Do you provide SEO?",
        "answer": "Yes — technical audits, on-page optimization, local SEO and ongoing content strategy, aimed at sustainable organic growth rather than quick tricks.",
        "order": 8,
    },
    {
        "question": "Do you work with small businesses?",
        "answer": "Yes. Our approach scales — small businesses get the same strategic process, sized to fit their budget and stage.",
        "order": 9,
    },
    {
        "question": "Do you work with e-commerce businesses?",
        "answer": "Yes — from first-time store launches to migrating off marketplaces onto an owned e-commerce platform.",
        "order": 10,
    },
    {
        "question": "Can you handle everything from website to marketing?",
        "answer": "Yes — that's the point of the Build, Grow, Brand, Optimize structure. One team carries strategy, design, development and marketing together, instead of handing you off between vendors.",
        "order": 11,
    },
    {
        "question": "How do I start a project?",
        "answer": "Reach out through the contact form or book a strategy call. We'll ask a few questions about your business and goals, then follow up with a tailored plan.",
        "order": 12,
    },
]


def seed(apps, schema_editor):
    FAQ = apps.get_model("faq", "FAQ")
    for faq in FAQS:
        FAQ.objects.get_or_create(question=faq["question"], defaults=faq)


def unseed(apps, schema_editor):
    FAQ = apps.get_model("faq", "FAQ")
    FAQ.objects.filter(question__in=[f["question"] for f in FAQS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
