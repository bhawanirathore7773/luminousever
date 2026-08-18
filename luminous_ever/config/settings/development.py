from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Emails print to the console instead of actually sending in dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
