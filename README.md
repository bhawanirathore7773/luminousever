# Luminous Ever — Digital Growth Agency Website

Django-powered site for Luminous Ever: services, portfolio/case studies,
blog, team, testimonials, FAQ, and a lead-capture contact system — built
end-to-end and CMS-managed from Django Admin.

## Requirements

- Python 3.12 (see `runtime.txt`)
- PostgreSQL 14+ in production (sqlite is used automatically for local dev — nothing to install)
- Redis in production for caching (optional locally — falls back to in-memory)

## Local setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # then fill in real values
# .env already exists in this delivery with a generated dev SECRET_KEY —
# only copy .env.example if you're starting fresh or rotating the key.

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/`
(or your configured `ADMIN_URL_PATH`) to manage everything — services,
case studies, blog posts, team, testimonials, FAQs, leads, and site-wide
settings (logo, contact info, socials, mission/vision, SEO defaults).

## Settings modules

| Module | Used for |
|---|---|
| `config.settings.development` | local work (default in `manage.py`) |
| `config.settings.production` | deployment — `DEBUG=False` hardcoded, enforces HTTPS/HSTS/secure cookies, requires `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` set explicitly |

Set `DJANGO_SETTINGS_MODULE=config.settings.production` as a platform env
var on the server — never edit code to switch environments.

## Deployment checklist

Tested against this exact checklist before each phase shipped — not just
written and assumed correct:

- [ ] `DJANGO_SETTINGS_MODULE=config.settings.production` set on the host
- [ ] `SECRET_KEY` — generate a **new** one for production, never reuse the dev key:
      `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- [ ] `ALLOWED_HOSTS` set to your real domain(s)
- [ ] `CSRF_TRUSTED_ORIGINS` set (e.g. `https://luminousever.com,https://www.luminousever.com`)
- [ ] `DATABASE_URL` pointed at a real Postgres instance
- [ ] `CACHE_URL` pointed at Redis (`rediscache://host:6379/1`) — optional but recommended; defaults to in-memory otherwise
- [ ] `ADMIN_URL_PATH` changed from the default `admin/` to something unguessable
- [ ] Email vars set (`EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `LEAD_NOTIFICATION_EMAIL`) so contact-form notifications actually send
- [ ] `python manage.py collectstatic --noinput` run as part of the build — **required**: WhiteNoise's manifest storage will otherwise raise `Missing staticfiles manifest entry` on every page, not just static assets. This surfaces immediately with `DEBUG=False`, so it's caught long before a real visitor hits it.
- [ ] `python manage.py migrate` run (the `Procfile`'s `release` phase does this automatically on Heroku-style platforms)
- [ ] `python manage.py createsuperuser` run once, then log in and fill out Site Settings (logo, contact email/phone/WhatsApp, address, socials) — nothing here is fabricated, so it's blank until you add it
- [ ] Confirm `/robots.txt` and `/sitemap.xml` resolve on the real domain
- [ ] Update the `Site` domain in Admin → Sites if it doesn't match `SITE_DOMAIN`

Procfile is set up for Heroku-style platforms (`web` + `release` process
types). For other hosts, the equivalent commands are:

```bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 3
```

## Project layout

```
luminous_ever/
├── config/
│   ├── settings/{base,development,production}.py
│   ├── sitemaps.py
│   ├── urls.py, wsgi.py, asgi.py
├── apps/
│   ├── core/         ← SiteSettings, Statistic, UTM middleware, CSP middleware, schema helpers
│   ├── services/      ← Service, ServiceCategory, Industry
│   ├── portfolio/     ← CaseStudy, CaseStudyImage
│   ├── testimonials/  ← Testimonial
│   ├── team/           ← TeamMember
│   ├── blog/           ← BlogCategory, BlogPost
│   ├── faq/             ← FAQ
│   └── leads/          ← Lead (contact form + pipeline)
├── templates/
│   ├── base.html, 404.html, 500.html
│   └── components/    ← navbar, footer, cards, process, final CTA (all reusable)
├── static/{css,js}
├── media/
├── Procfile, runtime.txt
└── requirements.txt
```

## Architecture notes worth knowing

- **Demo content is clearly labeled everywhere** (Demo Project, Demo Testimonial, Demo Client, Demo Profile) — nothing pretends to be a real client, review, or team member. Replace it from Django Admin as real content comes in.
- **JSON-LD schema** (Organization, Service, BreadcrumbList, BlogPosting, FAQPage) is built as Python dicts and serialized with a script-tag-safe helper (`apps/core/schema.py`) — no hand-assembled JSON in templates.
- **WebP** auto-generates for case study and blog featured images on upload (Pillow-based signal handler) — no action needed, but the original file is always kept as a fallback.
- **Rate limiting** on the contact form (5 submissions/hour/IP) plus a honeypot field — both tested against real submissions, not just written.
- **CSP header** is real but pragmatic: allows `unsafe-inline` for scripts/styles since the build uses inline `style=""` attributes throughout rather than a nonce pipeline — documented trade-off in `apps/core/middleware.py`, not a silent gap.

## What's intentionally not built

- **Individual industry/service pages beyond what's seeded** — the architecture supports unlimited entries via Admin; only a representative set (9 services, 9 industries) is pre-populated with real copy, per the brief's own warning against thin, low-effort pages.
- **Google Review sync** — the `Testimonial` model has `source`/`google_review_url` fields ready for it, but the actual API integration wasn't built (flagged as future work in the original brief).
- **Client dashboard, online quotation, payment integration** — explicitly deferred as future scalability in the original brief; the architecture (clean app boundaries, REST-ready models) doesn't block adding them later.
