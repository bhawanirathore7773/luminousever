"""Shared model field validators."""

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Permissive enough for international formats (incl. Indian +91 numbers
# written with spaces) while still rejecting obvious garbage input.
phone_validator = RegexValidator(
    regex=r"^[\d\s\+\-\(\)]{7,20}$",
    message="Enter a valid phone number.",
)

MAX_IMAGE_UPLOAD_MB = 5


def validate_image_file_size(file):
    """Admin-only uploads (no public file upload form exists on this
    site), so this is basic hygiene against accidental huge files rather
    than a hard security boundary."""
    max_bytes = MAX_IMAGE_UPLOAD_MB * 1024 * 1024
    if file.size > max_bytes:
        raise ValidationError(f"Image file too large — must be under {MAX_IMAGE_UPLOAD_MB}MB.")
