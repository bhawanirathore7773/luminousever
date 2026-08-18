from django.db import migrations

CATEGORIES = [
    {"name": "Build", "slug": "build", "tagline": "Digital foundations", "order": 1},
    {"name": "Grow", "slug": "grow", "tagline": "Traffic & customer acquisition", "order": 2},
    {"name": "Brand", "slug": "brand", "tagline": "Identity & creative", "order": 3},
    {"name": "Optimize", "slug": "optimize", "tagline": "Performance & automation", "order": 4},
]

SERVICES = [
    {
        "category": "build", "order": 1,
        "name": "Web Development", "slug": "web-development",
        "short_description": "Fast, secure, SEO-ready websites built on Django — not a page builder you'll outgrow.",
        "hero_subtitle": "A website that loads fast, ranks well, and gives you room to grow — without needing a developer for every small change.",
        "problem": "Most small business websites are slow, hard to update, and built on templates that start breaking the moment you need something custom. That costs you customers before they even see what you offer.",
        "solution": "We build on Django — a framework built for speed, security and long-term flexibility — with a CMS that lets you update content yourself, and an architecture that can grow into e-commerce, booking, or custom features later without a rebuild.",
        "features": [
            {"title": "Custom design, not a template", "description": "Every page is designed around your business, not squeezed into someone else's layout."},
            {"title": "Built-in SEO architecture", "description": "Clean URLs, structured data and fast load times from day one — not bolted on after launch."},
            {"title": "Editable from Django Admin", "description": "Update text, images and pages yourself, no developer needed for routine changes."},
            {"title": "Built to scale", "description": "The same foundation can grow into e-commerce, booking systems or customer portals later."},
        ],
        "technologies": ["Django", "Python", "PostgreSQL", "HTML5 & CSS3", "REST API", "Git"],
        "benefits": ["Loads fast on mobile and desktop", "Ranks better on Google from launch", "Easy to update without touching code", "Secure by default", "Scales as your business grows"],
        "who_its_for": ["Businesses replacing an outdated or slow website", "Startups launching their first real online presence", "Companies that have outgrown a page-builder site"],
        "deliverables": ["Fully responsive custom website", "Django Admin access for content updates", "Basic on-page SEO setup", "Google Analytics & Search Console integration", "30 days of post-launch support"],
        "faqs": [
            {"question": "How long does a website take to build?", "answer": "Most business websites launch in a few weeks from kickoff, depending on the number of pages and custom features involved."},
            {"question": "Can I update the website myself after launch?", "answer": "Yes — every site includes Django Admin access so you can edit text, images and pages without calling a developer."},
            {"question": "Will the website be optimized for Google?", "answer": "Yes, technical SEO — clean URLs, fast load times, structured data — is built in from the start, not added later."},
        ],
    },
    {
        "category": "build", "order": 2,
        "name": "E-commerce Development", "slug": "ecommerce",
        "short_description": "Online stores built to convert, with secure payments, inventory and a checkout that doesn't lose customers.",
        "hero_subtitle": "A store that makes buying easy — fast product pages, a smooth checkout, and the backend tools to manage it all yourself.",
        "problem": "A lot of e-commerce sites lose sales at checkout — too many steps, slow pages, or payment options customers don't trust. Every extra second and extra click costs conversions.",
        "solution": "We build e-commerce platforms on Django with a streamlined checkout, integrated payments, and an admin dashboard for managing products, orders and inventory — designed around reducing friction at every step.",
        "features": [
            {"title": "Streamlined checkout", "description": "Fewer steps between 'add to cart' and 'order confirmed', on both mobile and desktop."},
            {"title": "Secure payment integration", "description": "Trusted payment gateways (Razorpay and others) integrated directly into the checkout flow."},
            {"title": "Inventory & order management", "description": "Manage stock, pricing and orders from one admin dashboard."},
            {"title": "Mobile-first product pages", "description": "Product pages designed for how people actually shop on their phones."},
        ],
        "technologies": ["Django", "Python", "PostgreSQL", "Razorpay", "REST API", "Redis"],
        "benefits": ["Higher checkout completion rates", "Real-time inventory tracking", "Secure, trusted payment experience", "Room to add discounts, coupons and bundles later"],
        "who_its_for": ["Brands launching their first online store", "Businesses moving off marketplaces onto their own store", "Wholesalers adding a direct-to-consumer channel"],
        "deliverables": ["Full e-commerce storefront", "Payment gateway integration", "Product & inventory management dashboard", "Order tracking and notifications", "Mobile-optimized checkout"],
        "faqs": [
            {"question": "Which payment gateways do you support?", "answer": "Razorpay is our default integration for Indian businesses; other gateways can be added depending on your needs."},
            {"question": "Can I manage products myself after launch?", "answer": "Yes — the admin dashboard lets you add products, update pricing and track orders without developer help."},
            {"question": "Can the store integrate with marketplaces like Meesho or Flipkart?", "answer": "We can discuss marketplace integrations or parallel listing workflows depending on your existing catalog setup."},
        ],
    },
    {
        "category": "grow", "order": 1,
        "name": "SEO", "slug": "seo",
        "short_description": "Technical SEO, content strategy and local search — built to get found by people already looking for you.",
        "hero_subtitle": "Show up when your customers search — not just for your brand name, but for what you actually do.",
        "problem": "Ranking on Google isn't just about keywords — it's technical structure, content depth, backlinks and local signals working together. Most small business sites get one or two of these right and miss the rest.",
        "solution": "We run a full SEO program: technical audits, on-page optimization, content strategy and Google Business Profile management, so your site improves across every ranking factor Google actually weighs.",
        "features": [
            {"title": "Technical SEO audit", "description": "Site speed, crawlability, structured data and mobile usability, fixed at the source."},
            {"title": "On-page optimization", "description": "Titles, meta descriptions, headings and content structured around what people actually search."},
            {"title": "Local SEO & Google Business Profile", "description": "Optimized for 'near me' searches and local map pack visibility."},
            {"title": "Ongoing content strategy", "description": "Blog and page content planned around real search intent, not guesswork."},
        ],
        "technologies": ["Google Search Console", "Google Analytics", "Google Business Profile", "Schema.org markup"],
        "benefits": ["More organic (free) traffic over time", "Better visibility for local searches", "Higher-quality leads from intent-driven traffic", "Compounding results that don't stop when ad spend does"],
        "who_its_for": ["Businesses relying too heavily on paid ads", "Local businesses wanting to rank in their area", "Anyone whose website gets little to no organic traffic"],
        "deliverables": ["Technical SEO audit & fixes", "On-page optimization across key pages", "Google Business Profile setup/optimization", "Monthly performance reporting"],
        "faqs": [
            {"question": "How long does SEO take to show results?", "answer": "Meaningful movement typically takes a few months — SEO compounds over time rather than delivering overnight results."},
            {"question": "Do you guarantee first-page rankings?", "answer": "No one can honestly guarantee specific rankings — we focus on the technical and content fundamentals that drive sustainable growth."},
            {"question": "Is SEO better than running ads?", "answer": "They work differently — ads bring immediate traffic, SEO builds long-term visibility. Most businesses benefit from both."},
        ],
    },
    {
        "category": "grow", "order": 2,
        "name": "Google Ads", "slug": "google-ads",
        "short_description": "Search, display and shopping campaigns built around a target you actually care about: return on ad spend.",
        "hero_subtitle": "Paid traffic that's built to convert, not just click — with clear reporting on where every rupee goes.",
        "problem": "It's easy to spend money on Google Ads and hard to know if it's working. Poorly structured campaigns burn budget on the wrong keywords, with no clear read on what's actually converting.",
        "solution": "We build campaigns around your actual customer journey — the right keywords, tightly matched ad copy, and landing pages designed to convert — with reporting that shows exactly what's working.",
        "features": [
            {"title": "Keyword & intent research", "description": "Targeting people actively searching for what you offer, not just broad traffic."},
            {"title": "Campaign structure built for control", "description": "Organized ad groups and match types so budget isn't wasted on irrelevant clicks."},
            {"title": "Conversion tracking from day one", "description": "Know exactly which campaigns and keywords are driving leads or sales."},
            {"title": "Landing pages built to convert", "description": "Ad traffic lands somewhere designed to turn clicks into leads."},
        ],
        "technologies": ["Google Ads", "Google Analytics", "Google Tag Manager", "Conversion tracking"],
        "benefits": ["Immediate, measurable traffic", "Clear visibility into cost per lead", "Budget spent on people likely to convert", "Campaigns that improve as data accumulates"],
        "who_its_for": ["Businesses that need leads or sales quickly", "Anyone currently running ads with no clear ROI picture", "E-commerce brands wanting to scale paid traffic"],
        "deliverables": ["Campaign setup & structure", "Conversion tracking implementation", "Ad copy and creative direction", "Monthly performance reporting"],
        "faqs": [
            {"question": "What's a reasonable ad budget to start with?", "answer": "It depends on your industry and goals — we'll recommend a starting budget based on your market during onboarding."},
            {"question": "How is performance measured?", "answer": "Through conversion tracking tied to actual leads or sales, not just clicks or impressions."},
            {"question": "Do you manage the ad account or do I?", "answer": "We manage campaigns end-to-end, with full transparency and reporting access for you."},
        ],
    },
    {
        "category": "grow", "order": 3,
        "name": "Meta Ads", "slug": "meta-ads",
        "short_description": "Facebook & Instagram campaigns built around scroll-stopping creative and audiences that actually convert.",
        "hero_subtitle": "Reach the right people on Instagram and Facebook with creative that stops the scroll and offers that convert.",
        "problem": "Meta Ads reward creative that performs — most campaigns fail not because of bad targeting, but because the ad itself doesn't earn attention in a crowded feed.",
        "solution": "We combine audience strategy with creative built specifically for how people actually use Instagram and Facebook, then optimize continuously based on real performance data.",
        "features": [
            {"title": "Audience & retargeting strategy", "description": "Reaching people likely to convert, and re-engaging those who almost did."},
            {"title": "Scroll-stopping creative", "description": "Ad creative built for the feed and Reels format, not repurposed print ads."},
            {"title": "A/B testing built in", "description": "Multiple creative and copy variations tested to find what actually performs."},
            {"title": "Full-funnel campaigns", "description": "Awareness, consideration and conversion campaigns working together, not in isolation."},
        ],
        "technologies": ["Meta Ads Manager", "Meta Pixel", "Instagram & Facebook", "Conversion API"],
        "benefits": ["Precise audience targeting", "Creative built for how people actually scroll", "Clear cost-per-result tracking", "Retargeting that recovers near-misses"],
        "who_its_for": ["D2C and e-commerce brands", "Businesses with strong visual products", "Anyone wanting to build brand awareness alongside sales"],
        "deliverables": ["Campaign & audience setup", "Ad creative direction", "Meta Pixel & conversion tracking", "Monthly performance reporting"],
        "faqs": [
            {"question": "Do you create the ad creative too?", "answer": "Yes — creative direction and design are part of the service, built specifically for Instagram and Facebook formats."},
            {"question": "How is Meta Ads different from Google Ads?", "answer": "Google Ads targets active search intent; Meta Ads targets people based on interests and behavior — most brands benefit from using both."},
            {"question": "Can you also handle retargeting?", "answer": "Yes — retargeting past visitors and near-converters is usually one of the highest-return parts of a Meta Ads campaign."},
        ],
    },
    {
        "category": "grow", "order": 4,
        "name": "Social Media Management", "slug": "social-media",
        "short_description": "Consistent posting, creative and community management — so your brand looks alive everywhere it shows up.",
        "hero_subtitle": "A social presence that looks consistent, posts on schedule, and actually sounds like your brand.",
        "problem": "Inconsistent posting and off-brand creative make a business look inactive or amateur — even when the actual product or service is excellent.",
        "solution": "We handle content planning, creative production and posting on a consistent schedule, keeping every post aligned with your brand voice and visual identity.",
        "features": [
            {"title": "Content calendar & planning", "description": "Posts planned around your business goals, not last-minute scrambling."},
            {"title": "On-brand creative", "description": "Every post, reel and story follows the same visual identity as your website."},
            {"title": "Community management", "description": "Comments and DMs monitored and responded to promptly."},
            {"title": "Performance reporting", "description": "Clear monthly reporting on reach, engagement and growth."},
        ],
        "technologies": ["Instagram", "Facebook", "LinkedIn", "Scheduling & analytics tools"],
        "benefits": ["Consistent brand presence across platforms", "More engagement and follower growth", "Time saved not managing it in-house", "Content that builds trust before someone even visits your site"],
        "who_its_for": ["Businesses posting inconsistently or not at all", "Brands wanting a more professional social presence", "Anyone without time to manage social media in-house"],
        "deliverables": ["Monthly content calendar", "Post, reel and story creative", "Community management", "Monthly performance report"],
        "faqs": [
            {"question": "How many posts per week do you recommend?", "answer": "It depends on the platform and industry — we'll recommend a realistic, sustainable posting frequency during onboarding."},
            {"question": "Do you write captions too?", "answer": "Yes, captions are written to match your brand voice as part of the content package."},
            {"question": "Can you work with content I already have?", "answer": "Yes — we can incorporate existing photos, videos or brand assets into the content plan."},
        ],
    },
    {
        "category": "brand", "order": 1,
        "name": "Branding & Graphic Design", "slug": "branding",
        "short_description": "Visual identity, logo and design systems that make your brand instantly recognizable, everywhere it appears.",
        "hero_subtitle": "A visual identity that looks the same — and looks premium — on your website, your packaging and your Instagram feed.",
        "problem": "Inconsistent colors, fonts and logo usage across platforms make a business look unpolished, even when the product itself is great. Customers notice, even if they can't say exactly why.",
        "solution": "We build a complete visual identity system — logo, color palette, typography and usage guidelines — so every touchpoint looks like it belongs to the same brand.",
        "features": [
            {"title": "Logo & visual identity", "description": "A distinct mark and identity system built around your business, not a generic template."},
            {"title": "Brand guidelines", "description": "Clear rules for colors, typography and logo usage so consistency doesn't depend on memory."},
            {"title": "Marketing collateral", "description": "Templates for social posts, packaging, business cards and more."},
            {"title": "Design system for digital", "description": "The same identity carried consistently through your website and app interfaces."},
        ],
        "technologies": ["Adobe Creative Suite", "Figma", "Print & digital design"],
        "benefits": ["Instantly recognizable across platforms", "A more premium, trustworthy look", "Faster content creation with ready templates", "A brand that scales without losing consistency"],
        "who_its_for": ["New businesses building a brand from scratch", "Businesses with inconsistent or outdated visual identity", "Companies preparing to scale marketing and need a system, not one-off designs"],
        "deliverables": ["Logo suite (primary, secondary, icon)", "Brand color palette & typography", "Brand guidelines document", "Core marketing templates"],
        "faqs": [
            {"question": "Do you design logos from scratch?", "answer": "Yes — every identity is designed specifically for your business, not adapted from a template."},
            {"question": "What if I already have a logo I like?", "answer": "We can build a full brand system around an existing logo, or refine it as part of the process."},
            {"question": "Do you also design social media templates?", "answer": "Yes, ready-to-use templates for social posts are part of most branding packages."},
        ],
    },
    {
        "category": "optimize", "order": 1,
        "name": "Website Maintenance", "slug": "web-maintenance",
        "short_description": "Updates, security patches and monitoring so your site stays fast, safe and online — without you thinking about it.",
        "hero_subtitle": "One less thing to worry about — we keep your site updated, secure and running smoothly after launch.",
        "problem": "Websites don't stay secure or fast on their own. Skipped updates and unmonitored uptime are how small issues turn into a broken site or a security incident.",
        "solution": "We handle ongoing updates, security monitoring, backups and performance checks, so problems get caught and fixed before they affect visitors or customers.",
        "features": [
            {"title": "Security monitoring & patching", "description": "Dependencies and security settings kept current to reduce vulnerability risk."},
            {"title": "Regular backups", "description": "Automated backups so content and data are recoverable if something goes wrong."},
            {"title": "Uptime monitoring", "description": "Alerts if the site goes down, so issues are caught fast, not discovered by a customer."},
            {"title": "Performance checks", "description": "Periodic reviews to keep load times fast as content and traffic grow."},
        ],
        "technologies": ["Django", "PostgreSQL", "Server & uptime monitoring tools"],
        "benefits": ["Fewer security risks", "Faster average load times over time", "Peace of mind between larger projects", "Issues caught before visitors notice"],
        "who_its_for": ["Businesses with a live site and no dedicated developer", "Anyone who has been putting off updates", "Sites handling customer data or payments"],
        "deliverables": ["Monthly security & dependency updates", "Automated backup schedule", "Uptime monitoring & alerts", "Quarterly performance review"],
        "faqs": [
            {"question": "What happens if my site goes down?", "answer": "Uptime monitoring alerts us immediately so we can investigate and fix the issue as fast as possible."},
            {"question": "Is maintenance required, or optional?", "answer": "It's optional but strongly recommended — most security and performance issues are far cheaper to prevent than to fix after the fact."},
            {"question": "Can you take over maintenance for a site you didn't build?", "answer": "In most cases yes, after a short technical review to understand the existing setup."},
        ],
    },
    {
        "category": "optimize", "order": 2,
        "name": "Automation", "slug": "automation",
        "short_description": "WhatsApp lead automation, email workflows and CRM connections that save time on repetitive follow-up.",
        "hero_subtitle": "Automate the repetitive follow-up so leads get a response in minutes, not whenever someone gets to it.",
        "problem": "Slow follow-up loses leads — but manually responding to every inquiry, form submission or WhatsApp message doesn't scale as the business grows.",
        "solution": "We set up automated workflows — instant WhatsApp responses, lead routing, email sequences — so every inquiry gets a fast, consistent response without needing a person watching every channel.",
        "features": [
            {"title": "WhatsApp lead automation", "description": "Instant automated responses to new inquiries, with handoff to a real person when needed."},
            {"title": "Lead routing & notifications", "description": "New leads automatically tagged, notified and routed to the right person."},
            {"title": "Email follow-up sequences", "description": "Automated nurture sequences that keep leads warm without manual effort."},
            {"title": "CRM & tool integrations", "description": "Connecting your website, WhatsApp and lead tracking into one system."},
        ],
        "technologies": ["WhatsApp Business API", "Email automation tools", "Webhooks & integrations"],
        "benefits": ["Faster response times on new leads", "Fewer inquiries falling through the cracks", "Time saved on repetitive manual follow-up", "A clearer picture of where leads come from"],
        "who_its_for": ["Businesses getting inquiries across multiple channels", "Teams currently following up manually", "Anyone losing leads to slow response times"],
        "deliverables": ["WhatsApp automation setup", "Lead routing & notification workflow", "Email follow-up sequence", "Basic CRM/integration setup"],
        "faqs": [
            {"question": "Do I need a WhatsApp Business account already?", "answer": "It helps, but we can guide you through setting one up as part of the process."},
            {"question": "Will automation replace real conversations with customers?", "answer": "No — automation handles the instant first response and routing; real conversations still happen with a real person."},
            {"question": "Can this connect to a CRM I already use?", "answer": "In most cases yes — we'll review your current tools during setup and connect where possible."},
        ],
    },
]

INDUSTRIES = [
    {
        "name": "Retail", "slug": "retail", "order": 1,
        "description": "Retail businesses compete on discovery as much as price — customers need to find you online before they ever walk in or check out. We help retail brands build a digital presence that drives both foot traffic and online sales.",
        "challenges": ["Competing with marketplaces on visibility", "Keeping online and in-store branding consistent", "Turning local searches into store visits or online orders"],
        "services": ["web-development", "seo", "social-media", "google-ads"],
    },
    {
        "name": "E-commerce", "slug": "e-commerce", "order": 2,
        "description": "For e-commerce brands, the website isn't a brochure — it's the entire sales channel. Every second of load time and every extra checkout step directly affects revenue. We build stores designed to convert, and the marketing systems to keep bringing customers back.",
        "challenges": ["Cart abandonment and checkout friction", "Standing out in a crowded online market", "Balancing paid acquisition cost against margins"],
        "services": ["ecommerce", "meta-ads", "google-ads", "seo"],
    },
    {
        "name": "Manufacturing", "slug": "manufacturing", "order": 3,
        "description": "B2B manufacturing buyers research extensively before ever making contact — if your business isn't visible and credible online, you're not even in the conversation. We help manufacturers build a digital presence that generates serious inbound inquiries.",
        "challenges": ["Long, research-heavy B2B buying cycles", "Communicating technical capability clearly online", "Generating qualified inquiries, not just traffic"],
        "services": ["web-development", "seo", "branding"],
    },
    {
        "name": "Real Estate", "slug": "real-estate", "order": 4,
        "description": "Property buyers form their first impression online, long before a site visit. We help real estate businesses build listings-focused websites and lead systems that convert browsers into serious inquiries.",
        "challenges": ["Showcasing properties compellingly online", "Capturing and following up on leads quickly", "Standing out in a highly visual, competitive market"],
        "services": ["web-development", "seo", "automation", "meta-ads"],
    },
    {
        "name": "Healthcare", "slug": "healthcare", "order": 5,
        "description": "Patients research providers online before booking — trust, clarity and accurate information matter more here than almost any other industry. We build healthcare websites focused on credibility, accessibility and easy appointment inquiries.",
        "challenges": ["Building trust and credibility online", "Making appointment inquiries simple and fast", "Local visibility for 'near me' healthcare searches"],
        "services": ["web-development", "seo", "automation"],
    },
    {
        "name": "Hospitality", "slug": "hospitality", "order": 6,
        "description": "For restaurants, hotels and hospitality businesses, visuals and reviews do most of the convincing. We build visually strong websites and social presences that make the experience obvious before someone ever walks in.",
        "challenges": ["Standing out visually in a crowded local market", "Managing bookings and inquiries efficiently", "Keeping social content fresh and consistent"],
        "services": ["web-development", "social-media", "branding", "meta-ads"],
    },
    {
        "name": "Professional Services", "slug": "professional-services", "order": 7,
        "description": "Professional services businesses — legal, consulting, financial and beyond — sell trust and expertise. We build websites and content that establish credibility and make it easy for the right clients to reach out.",
        "challenges": ["Communicating expertise clearly to non-experts", "Standing out from similarly positioned competitors", "Generating qualified inquiries, not just traffic"],
        "services": ["web-development", "seo", "branding"],
    },
    {
        "name": "Fashion", "slug": "fashion", "order": 8,
        "description": "Fashion brands live and die by visual presentation and social presence. We build stores and content systems that make the product the hero, backed by a checkout experience that doesn't lose the sale.",
        "challenges": ["Presenting products compellingly online", "Keeping up with fast-moving trends and content demand", "Converting social attention into actual sales"],
        "services": ["ecommerce", "social-media", "branding", "meta-ads"],
    },
    {
        "name": "Startups", "slug": "startups", "order": 9,
        "description": "Startups need to move fast and look credible before the product or traction fully catches up. We help early-stage businesses build a digital presence that supports fundraising, early customers and rapid iteration.",
        "challenges": ["Looking credible with limited budget and time", "Building for speed without accumulating technical debt", "Establishing early trust and visibility"],
        "services": ["web-development", "branding", "seo"],
    },
]


def seed(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Industry = apps.get_model("services", "Industry")

    category_objs = {}
    for cat in CATEGORIES:
        obj, _ = ServiceCategory.objects.get_or_create(slug=cat["slug"], defaults=cat)
        category_objs[cat["slug"]] = obj

    service_objs = {}
    for svc in SERVICES:
        data = {**svc}
        cat_slug = data.pop("category")
        data["category_id"] = category_objs[cat_slug].id
        slug = data["slug"]
        obj, _ = Service.objects.get_or_create(slug=slug, defaults=data)
        service_objs[slug] = obj

    for ind in INDUSTRIES:
        data = {**ind}
        service_slugs = data.pop("services")
        obj, created = Industry.objects.get_or_create(slug=ind["slug"], defaults=data)
        if created:
            obj.relevant_services.set([service_objs[s] for s in service_slugs if s in service_objs])


def unseed(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Industry = apps.get_model("services", "Industry")
    Industry.objects.filter(slug__in=[i["slug"] for i in INDUSTRIES]).delete()
    Service.objects.filter(slug__in=[s["slug"] for s in SERVICES]).delete()
    ServiceCategory.objects.filter(slug__in=[c["slug"] for c in CATEGORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
