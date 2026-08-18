from django.db import migrations
from django.utils.html import strip_tags

CATEGORIES = [
    {"name": "Digital Marketing", "slug": "digital-marketing", "order": 1},
    {"name": "SEO", "slug": "seo", "order": 2},
    {"name": "Web Development", "slug": "web-development", "order": 3},
    {"name": "E-commerce", "slug": "e-commerce", "order": 4},
    {"name": "Social Media", "slug": "social-media", "order": 5},
    {"name": "Business Growth", "slug": "business-growth", "order": 6},
    {"name": "Branding", "slug": "branding", "order": 7},
    {"name": "Technology", "slug": "technology", "order": 8},
]

POSTS = [
    {
        "title": "Why Your Business Website Needs More Than a Homepage",
        "slug": "website-needs-more-than-a-homepage",
        "category": "web-development",
        "excerpt": "A single-page website might look fine at first glance, but it's quietly costing you visibility, credibility and leads.",
        "content": """
<p>A lot of small business websites are really just one page with a few sections stacked on top of each other — a hero, some services, a contact form. It looks fine. But it's not actually doing the job a website is supposed to do.</p>
<h2>Google can't rank what doesn't exist</h2>
<p>Search engines rank pages, not websites. If you offer five services but only have one page mentioning all of them in a sentence each, you have almost no chance of ranking for any of them individually. Someone searching for a specific service is looking for a page about that service — not a homepage that mentions it once.</p>
<h2>Visitors need somewhere to land</h2>
<p>When someone clicks an ad or a search result for a specific service, they expect to land on a page about that service — not your homepage, where they have to scroll and hunt for relevant information. That mismatch is one of the fastest ways to lose a visitor.</p>
<h2>What a real website structure looks like</h2>
<p>At minimum, a business website should have: a homepage, individual pages for each core service, an about page, a portfolio or case studies section, and a contact page built for actually capturing leads. Each page exists to answer a specific question a visitor — or Google — is asking.</p>
<h2>The fix doesn't have to be a full rebuild</h2>
<p>If your website is currently a single page, the fix is usually to break out your existing content into dedicated pages, not to start over. It's a smaller project than it sounds, and it's often the single highest-leverage change you can make to how the site performs.</p>
""",
        "meta_title": "Why Your Website Needs More Than a Homepage",
        "meta_description": "A single-page website limits your SEO and conversions. Here's why dedicated service and landing pages matter for small business growth.",
    },
    {
        "title": "Local SEO Basics Every Small Business Should Know",
        "slug": "local-seo-basics-for-small-business",
        "category": "seo",
        "excerpt": "If your business serves a local area, showing up in local search results matters more than ranking nationally. Here's where to start.",
        "content": """
<p>For most local businesses, ranking #1 nationally for a broad keyword matters far less than showing up when someone nearby searches "near me." Local SEO is a different game with its own rules — and most small businesses are only doing part of it.</p>
<h2>Claim and complete your Google Business Profile</h2>
<p>This is the single highest-leverage thing most local businesses skip. A complete, accurate Google Business Profile — hours, category, photos, service area — directly affects whether you show up in the local map pack.</p>
<h2>Consistency matters more than volume</h2>
<p>Your business name, address and phone number should match exactly everywhere they appear online — your website, Google, directories, social profiles. Inconsistent details confuse search engines about whether it's really the same business.</p>
<h2>Reviews are a ranking factor, not just social proof</h2>
<p>The number, recency and quality of reviews on your Google Business Profile genuinely affect local rankings — not just whether a customer trusts you before they click.</p>
<h2>Where to start</h2>
<p>If you're only going to do one thing this month, make it your Google Business Profile. It's free, it's fast, and for most small businesses, it's the biggest gap.</p>
""",
        "meta_title": "Local SEO Basics for Small Businesses",
        "meta_description": "Local SEO fundamentals every small business should have in place — Google Business Profile, NAP consistency, reviews, and more.",
    },
    {
        "title": "Google Ads vs Meta Ads: Which Should You Start With?",
        "slug": "google-ads-vs-meta-ads",
        "category": "digital-marketing",
        "excerpt": "Both can work — but they work differently, and starting with the wrong one for your business can waste budget before you learn anything useful.",
        "content": """
<p>This is one of the most common questions we get from businesses running ads for the first time, and the honest answer is: it depends on how your customers actually search for and discover what you sell.</p>
<h2>Google Ads targets intent</h2>
<p>Someone searching for a specific service is actively looking for a solution right now. Google Ads is strongest when people already know they want what you offer and are searching for it — services, urgent needs, comparison shopping.</p>
<h2>Meta Ads targets attention</h2>
<p>Instagram and Facebook users aren't searching for you — they're scrolling. Meta Ads works by interrupting that scroll with something visually compelling enough to stop for. It's stronger for visual products and building awareness before someone is actively searching.</p>
<h2>A simple way to decide</h2>
<p>If people actively search for what you sell, start with Google Ads. If your product is visual and benefits from discovery, Meta Ads often performs better early on.</p>
<h2>Most businesses eventually need both</h2>
<p>Google Ads captures demand that already exists. Meta Ads helps create it. As budget allows, most businesses get the most value from running both together.</p>
""",
        "meta_title": "Google Ads vs Meta Ads: Where to Start",
        "meta_description": "Google Ads and Meta Ads work differently. Here's how to decide which one to start with based on how your customers actually find you.",
    },
    {
        "title": "5 Signs Your E-commerce Checkout Is Losing You Sales",
        "slug": "ecommerce-checkout-losing-sales",
        "category": "e-commerce",
        "excerpt": "A surprising amount of e-commerce revenue is lost not to bad products or high prices, but to friction in the last 60 seconds of the buying process.",
        "content": """
<p>If your product pages get healthy traffic but sales don't match, the issue is often not the product — it's what happens between "add to cart" and "order confirmed."</p>
<h2>1. Too many steps before payment</h2>
<p>Every extra screen between cart and payment is a chance for someone to abandon. Account creation, shipping details, billing details, confirmation — each as a separate page — adds up fast.</p>
<h2>2. Forcing account creation</h2>
<p>Requiring a full account before checkout is one of the most common, most fixable causes of abandoned carts. A guest checkout option almost always recovers some of that lost revenue.</p>
<h2>3. Limited or unfamiliar payment options</h2>
<p>If customers don't see a payment method they trust and recognize, some will simply leave rather than enter card details on an unfamiliar gateway.</p>
<h2>4. Slow load times at the worst possible moment</h2>
<p>A slow checkout page is worse than a slow homepage — it interrupts someone at the exact moment they were ready to buy.</p>
<h2>5. No visible trust signals</h2>
<p>Security badges, clear return policies, and visible contact information reduce last-minute hesitation, especially for first-time buyers.</p>
""",
        "meta_title": "5 E-commerce Checkout Mistakes Costing You Sales",
        "meta_description": "Common checkout friction points that cause cart abandonment — and how to fix them without a full e-commerce rebuild.",
    },
    {
        "title": "Building a Consistent Brand Across Every Platform",
        "slug": "consistent-brand-across-platforms",
        "category": "branding",
        "excerpt": "Your logo isn't your brand. Consistency — the same look, tone and feel everywhere a customer encounters you — is what actually builds recognition.",
        "content": """
<p>A lot of businesses think of branding as "getting a logo made." A logo is one piece of a much bigger system — and inconsistency in the rest of that system is what makes a business feel unpolished, even with a great logo.</p>
<h2>What actually needs to be consistent</h2>
<p>Colors, typography, tone of voice, and the general visual style of photos and graphics — all of it, applied the same way whether someone sees your website, your Instagram, or your packaging.</p>
<h2>Why this is harder than it sounds</h2>
<p>Without documented guidelines, consistency depends on whoever happens to be creating content that week remembering exactly how things were done last time. That breaks down fast, especially once more than one person is involved.</p>
<h2>Guidelines don't have to be complicated</h2>
<p>A simple one-page reference — exact colors, approved fonts, a few example applications — is usually enough to keep everyone aligned, whether that's an internal team member or a freelancer helping with a single project.</p>
<h2>Consistency compounds</h2>
<p>The value of a consistent brand isn't obvious in any single post or page — it's the effect of seeing the same look repeatedly that builds recognition and trust over time.</p>
""",
        "meta_title": "Building Brand Consistency Across Every Platform",
        "meta_description": "A logo isn't a brand. Here's what actually needs to stay consistent across your website, social media and marketing materials.",
    },
    {
        "title": "Why Fast Lead Response Time Matters More Than You Think",
        "slug": "fast-lead-response-time",
        "category": "business-growth",
        "excerpt": "The single biggest factor in whether a lead converts often isn't your pricing or your pitch — it's how fast you responded.",
        "content": """
<p>It's easy to focus on getting more leads and overlook what happens in the minutes right after someone submits an inquiry. That window matters more than most businesses realize.</p>
<h2>Interest fades fast</h2>
<p>Someone who just filled out a form or messaged on WhatsApp is at their most interested right now. Every hour that passes, that interest cools — and they're often contacting other options in the meantime.</p>
<h2>Manual follow-up doesn't scale</h2>
<p>If every inquiry depends on someone being available to notice and respond, response time becomes inconsistent — fast when things are quiet, slow when the team is busy with other work.</p>
<h2>Automation handles the first response, not the whole conversation</h2>
<p>An automated instant acknowledgment — confirming the inquiry was received and setting expectations for next steps — closes that critical gap, even before a real person picks up the conversation.</p>
<h2>The upside is measurable</h2>
<p>Faster response time doesn't just feel better for the customer — it directly improves how many inquiries actually convert into paying clients.</p>
""",
        "meta_title": "Why Fast Lead Response Time Matters",
        "meta_description": "Response speed is one of the biggest, most overlooked factors in lead conversion. Here's why it matters and how automation helps.",
    },
]


def seed(apps, schema_editor):
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost = apps.get_model("blog", "BlogPost")

    category_objs = {}
    for cat in CATEGORIES:
        obj, _ = BlogCategory.objects.get_or_create(slug=cat["slug"], defaults=cat)
        category_objs[cat["slug"]] = obj

    for post in POSTS:
        data = {**post}
        cat_slug = data.pop("category")
        data["category_id"] = category_objs[cat_slug].id
        word_count = len(strip_tags(data["content"]).split())
        data["reading_time"] = max(1, round(word_count / 200))
        BlogPost.objects.get_or_create(slug=data["slug"], defaults=data)


def unseed(apps, schema_editor):
    BlogCategory = apps.get_model("blog", "BlogCategory")
    BlogPost = apps.get_model("blog", "BlogPost")
    BlogPost.objects.filter(slug__in=[p["slug"] for p in POSTS]).delete()
    BlogCategory.objects.filter(slug__in=[c["slug"] for c in CATEGORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
