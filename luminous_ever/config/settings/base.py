"""
Base settings for the Luminous Ever project.
Shared by development.py and production.py — never used directly.
"""

from pathlib import Path
import environ

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
# config/settings/base.py -> config/settings -> config -> project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------------------
# Environment variables (.env is loaded here; never commit it)
# ---------------------------------------------------------------------------
env = environ.Env(
    DEBUG=(bool, False),
)
ENV_FILE = BASE_DIR / ".env"
if ENV_FILE.exists():
    environ.Env.read_env(ENV_FILE)

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

SITE_NAME = env("SITE_NAME", default="Luminous Ever")
SITE_DOMAIN = env("SITE_DOMAIN", default="localhost:8000")

# ---------------------------------------------------------------------------
# Security (Phase 12) — applies in dev and prod. HTTPS-only cookie flags
# (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE) live in production.py since
# local dev runs over plain HTTP.
# ---------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True  # Django default; explicit for clarity
CSRF_COOKIE_HTTPONLY = True  # no JS on this site reads the CSRF cookie directly

# Change this in production so /admin/ isn't at a guessable, well-known
# path — set ADMIN_URL_PATH in .env, e.g. "backstage-4f2a/".
ADMIN_URL_PATH = env("ADMIN_URL_PATH", default="admin/")

# ---------------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
]

LOCAL_APPS = [
    "apps.core",
    "apps.services",
    "apps.portfolio",
    "apps.testimonials",
    "apps.team",
    "apps.blog",
    "apps.leads",
    "apps.faq",
    "apps.seo",
]

THIRD_PARTY_APPS = [
    # added as needed (e.g. django-ckeditor for blog, etc.)
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.UTMTrackingMiddleware",
    "apps.core.middleware.ContentSecurityPolicyMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ---------------------------------------------------------------------------
# Database — reads DATABASE_URL, falls back to sqlite for local dev
# ---------------------------------------------------------------------------
DATABASES = {
    "default": env.db(
        "DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# ---------------------------------------------------------------------------
# Cache — reads CACHE_URL, falls back to in-memory cache for local dev
# (no Redis server required to run this locally). In production, set
# CACHE_URL=rediscache://127.0.0.1:6379/1 (or your managed Redis URL).
# ---------------------------------------------------------------------------
CACHES = {
    "default": env.cache("CACHE_URL", default="locmemcache://"),
}
CACHE_MIDDLEWARE_SECONDS = env.int("CACHE_MIDDLEWARE_SECONDS", default=60 * 15)  # 15 min

# ---------------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = env("TIME_ZONE", default="Asia/Kolkata")
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------------
# Static & media files
# ---------------------------------------------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------
# Email (lead notifications) — console backend overridden in dev/prod
# ---------------------------------------------------------------------------
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="hello@luminousever.com")
LEAD_NOTIFICATION_EMAIL = env("LEAD_NOTIFICATION_EMAIL", default="hello@luminousever.com")

# ---------------------------------------------------------------------------
# Business contact details (used in schema.org / footer / templates)
# ---------------------------------------------------------------------------
BUSINESS_WHATSAPP_NUMBER = env("BUSINESS_WHATSAPP_NUMBER", default="")
BUSINESS_PHONE_NUMBER = env("BUSINESS_PHONE_NUMBER", default="")
GOOGLE_ANALYTICS_ID = env("GOOGLE_ANALYTICS_ID", default="")
META_PIXEL_ID = env("META_PIXEL_ID", default="")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "[{asctime}] {levelname} {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "verbose",
        },
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
        "apps": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": False},
    },
}
