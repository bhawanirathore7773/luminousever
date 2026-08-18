from django.db import migrations

CASE_STUDIES = [
    {
        "title": "Premium Fashion Brand", "slug": "premium-fashion-brand",
        "client_name": "Demo Fashion Brand", "industry": "fashion", "category": "branding",
        "services": ["branding", "social-media"],
        "short_description": "A cohesive brand identity system across website, packaging and social.",
        "challenge": "A growing fashion label had strong products but a visual identity that felt inconsistent across their website, packaging and Instagram — making the brand feel less premium than the product itself.",
        "objective": "Build a cohesive visual identity and refreshed digital presence that matched the quality of the product, without losing the brand's existing following.",
        "strategy": "Develop a complete brand system first, then apply it consistently across the website, social templates and packaging touchpoints.",
        "solution": "A refined logo, a considered color and type system, and a set of ready-to-use social templates — all documented in brand guidelines the internal team could apply themselves going forward.",
        "results": "A more cohesive brand presence across every touchpoint, with the internal team now able to produce on-brand content independently using the new guidelines.",
        "technologies": ["Figma", "Adobe Creative Suite", "Django"],
        "testimonial_quote": "The brand finally feels as premium as the product. Everything looks like it belongs together now.",
        "testimonial_author": "P. Malhotra", "testimonial_role": "Founder, Demo Fashion Brand",
    },
    {
        "title": "Local Manufacturing Business", "slug": "local-manufacturing-business",
        "client_name": "Demo Manufacturing Co.", "industry": "manufacturing", "category": "websites",
        "services": ["web-development", "seo"],
        "short_description": "A credible B2B web presence built to generate serious inbound inquiries.",
        "challenge": "A manufacturing business relied entirely on word-of-mouth and had no real online presence, making it invisible to buyers researching suppliers online before making contact.",
        "objective": "Establish a credible digital presence that could support inbound B2B inquiries and communicate technical capability clearly.",
        "strategy": "Build a website structured around capability, certifications and past work, paired with technical SEO to appear for relevant B2B search terms.",
        "solution": "A Django-built site with dedicated capability and product pages, structured data for search visibility, and a simple inquiry form connected to the sales team.",
        "results": "A functioning digital front door for the business — inbound inquiries now arrive through the website instead of relying solely on referrals.",
        "technologies": ["Django", "PostgreSQL", "Google Search Console"],
        "testimonial_quote": "We finally show up when people search for what we actually make.",
        "testimonial_author": "V. Reddy", "testimonial_role": "Operations Head, Demo Manufacturing Co.",
    },
    {
        "title": "D2C E-commerce Brand", "slug": "d2c-ecommerce-brand",
        "client_name": "Demo E-commerce Brand", "industry": "e-commerce", "category": "ecommerce",
        "services": ["ecommerce", "meta-ads"],
        "short_description": "An owned e-commerce channel with a streamlined mobile checkout.",
        "challenge": "A direct-to-consumer brand was selling through marketplaces but had no owned e-commerce channel, limiting margins and customer data ownership.",
        "objective": "Launch a fast, conversion-focused online store to build a direct sales channel alongside existing marketplace presence.",
        "strategy": "Prioritize a streamlined mobile checkout and fast product pages, backed by a Meta Ads strategy to drive initial traffic and retargeting.",
        "solution": "A Django e-commerce build with Razorpay integration, mobile-first product pages, and a Meta Ads campaign structured around awareness and retargeting.",
        "results": "A functioning owned sales channel with a measurably smoother checkout experience than the brand's previous marketplace-only presence.",
        "technologies": ["Django", "Razorpay", "Meta Ads Manager"],
        "testimonial_quote": "Having our own store changed how we think about the business — we finally own the customer relationship.",
        "testimonial_author": "N. Bansal", "testimonial_role": "Co-founder, Demo E-commerce Brand",
    },
    {
        "title": "Professional Services Firm", "slug": "professional-services-firm",
        "client_name": "Demo Professional Services Firm", "industry": "professional-services", "category": "seo",
        "services": ["web-development", "seo"],
        "short_description": "A rebuilt website that communicates expertise instead of undermining it.",
        "challenge": "A professional services firm had a dated website that undersold their expertise and made it hard for prospective clients to understand what made them different.",
        "objective": "Rebuild the website to clearly communicate expertise and credibility, and make it easy for qualified prospects to reach out.",
        "strategy": "Restructure content around client outcomes rather than generic service lists, paired with on-page SEO for relevant search terms.",
        "solution": "A redesigned Django site with clearer service pages, case-study style proof points, and a simple, low-friction contact process.",
        "results": "A website that better reflects the firm's actual expertise, with more qualified inquiries coming through the contact form.",
        "technologies": ["Django", "Google Analytics", "Google Search Console"],
        "testimonial_quote": "Prospects now understand what we do and why it matters before they even call us.",
        "testimonial_author": "K. Nair", "testimonial_role": "Managing Partner, Demo Professional Services Firm",
    },
    {
        "title": "Restaurant & Hospitality", "slug": "restaurant-hospitality",
        "client_name": "Demo Hospitality Business", "industry": "hospitality", "category": "social-media",
        "services": ["social-media", "branding"],
        "short_description": "A consistent, visually strong social presence that reflects the real experience.",
        "challenge": "A hospitality business had inconsistent, infrequent social posting that didn't reflect the actual experience of visiting — making it hard to stand out locally.",
        "objective": "Build a consistent, visually strong social presence that captures the actual experience and drives more local bookings and visits.",
        "strategy": "Establish a content calendar and visual identity for social, with a steady mix of ambience, menu and behind-the-scenes content.",
        "solution": "A monthly content calendar, on-brand creative templates, and consistent posting across Instagram and Facebook.",
        "results": "A noticeably more active, consistent social presence, with engagement and local visibility improving month over month.",
        "technologies": ["Instagram", "Facebook", "Scheduling & analytics tools"],
        "testimonial_quote": "Our page finally looks as good as the place actually feels.",
        "testimonial_author": "T. Verma", "testimonial_role": "Owner, Demo Hospitality Business",
    },
    {
        "title": "Real Estate Business", "slug": "real-estate-business",
        "client_name": "Demo Real Estate Business", "industry": "real-estate", "category": "ads",
        "services": ["seo", "web-development"],
        "short_description": "A trackable, systematic lead pipeline replacing ad hoc inquiries.",
        "challenge": "A real estate business was generating leads through informal channels only, with no systematic way to capture and follow up on online inquiries.",
        "objective": "Build a lead-generation focused digital presence and paid campaign structure to capture and convert serious buyer inquiries.",
        "strategy": "Pair a listings-focused website with targeted Google Ads campaigns and fast automated follow-up on new inquiries.",
        "solution": "A Django site built around property listings and lead capture, connected to Google Ads campaigns and an automated first-response workflow.",
        "results": "A steady, trackable flow of inbound inquiries, replacing the previous ad hoc, hard-to-measure lead process.",
        "technologies": ["Django", "Google Ads", "WhatsApp automation"],
        "testimonial_quote": "We can finally see where our leads are actually coming from.",
        "testimonial_author": "D. Chawla", "testimonial_role": "Director, Demo Real Estate Business",
    },
    {
        "title": "Healthcare Brand", "slug": "healthcare-brand",
        "client_name": "Demo Healthcare Provider", "industry": "healthcare", "category": "websites",
        "services": ["web-development", "automation"],
        "short_description": "A clearer, more trustworthy site with a simpler appointment inquiry flow.",
        "challenge": "A healthcare provider's website made it difficult for prospective patients to find clear information or book an appointment, undermining trust before a first visit.",
        "objective": "Rebuild the website around clarity, trust and a simple appointment inquiry process.",
        "strategy": "Simplify information architecture, add clear credentials and service information, and streamline the appointment inquiry flow.",
        "solution": "A redesigned Django site with clear service and credential pages, and an automated inquiry workflow routing requests promptly.",
        "results": "A clearer, more trustworthy online presence with a simpler path from visitor to booked inquiry.",
        "technologies": ["Django", "Automation workflows", "Google Business Profile"],
        "testimonial_quote": "Patients tell us the website makes it easy to know what to expect before they even call.",
        "testimonial_author": "M. Rao", "testimonial_role": "Practice Manager, Demo Healthcare Provider",
    },
    {
        "title": "Startup Launch", "slug": "startup-launch",
        "client_name": "Demo Startup", "industry": "startups", "category": "creative",
        "services": ["branding", "web-development"],
        "short_description": "A credible early-stage brand and website built to scale, not be rebuilt.",
        "challenge": "An early-stage startup needed to look credible to investors and early customers well before their product roadmap had fully caught up.",
        "objective": "Establish a credible brand and digital presence quickly, on a limited early-stage budget and timeline.",
        "strategy": "Focus on a clean, confident brand identity and a fast, well-structured website that can evolve as the product and team grow.",
        "solution": "A lean but polished brand identity paired with a Django website built to be extended, not rebuilt, as the startup scales.",
        "results": "A credible public presence in place ahead of early fundraising and customer conversations, built on a foundation that scales.",
        "technologies": ["Django", "Figma", "Google Analytics"],
        "testimonial_quote": "It gave us something credible to point people to from day one.",
        "testimonial_author": "A. Joshi", "testimonial_role": "Founder, Demo Startup",
    },
]


def seed(apps, schema_editor):
    CaseStudy = apps.get_model("portfolio", "CaseStudy")
    Industry = apps.get_model("services", "Industry")
    Service = apps.get_model("services", "Service")

    for order, cs in enumerate(CASE_STUDIES, start=1):
        data = {**cs}
        industry_slug = data.pop("industry")
        service_slugs = data.pop("services")
        data["order"] = order
        try:
            data["industry_id"] = Industry.objects.get(slug=industry_slug).id
        except Industry.DoesNotExist:
            data["industry_id"] = None

        obj, created = CaseStudy.objects.get_or_create(slug=cs["slug"], defaults=data)
        if created:
            services = Service.objects.filter(slug__in=service_slugs)
            obj.services.set(services)


def unseed(apps, schema_editor):
    CaseStudy = apps.get_model("portfolio", "CaseStudy")
    CaseStudy.objects.filter(slug__in=[c["slug"] for c in CASE_STUDIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
        ("services", "0002_seed_services_and_industries"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
