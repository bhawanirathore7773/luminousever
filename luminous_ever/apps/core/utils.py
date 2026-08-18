"""Shared utilities."""

import io

from django.core.files.base import ContentFile
from PIL import Image


def generate_webp_content(image_field, quality=82):
    """
    Given a Django ImageFieldFile, returns (filename, ContentFile) with a
    WebP-encoded version of the same image, or None if conversion isn't
    possible (corrupt file, unsupported mode, etc.) — WebP is always an
    optimization on top of the original, never a hard requirement for
    saving it.
    """
    if not image_field:
        return None
    try:
        image_field.open()
        image_field.seek(0)
        img = Image.open(image_field)
        img = img.convert("RGBA") if img.mode in ("RGBA", "LA", "P") else img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, format="WEBP", quality=quality)
        buffer.seek(0)
        base_name = image_field.name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        return f"{base_name}.webp", ContentFile(buffer.read())
    except Exception:
        return None
