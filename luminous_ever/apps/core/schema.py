"""
JSON-LD helpers shared across apps. Building these as Python dicts and
serializing with json.dumps — rather than hand-assembling JSON-LD directly
in templates with conditional commas — avoids trailing-comma bugs when
optional fields are missing.
"""

import json

# Escapes that prevent a JSON string from being able to break out of its
# enclosing <script> tag (e.g. a field containing literal "</script>"
# text). Same technique Django's own json_script template filter uses
# internally — plain json.dumps() does not do this on its own.
_SCRIPT_BREAKOUT_ESCAPES = {
    ord("<"): "\\u003C",
    ord(">"): "\\u003E",
    ord("&"): "\\u0026",
}


def safe_json_dumps(data):
    """json.dumps, but safe to embed inside <script type="application/ld+json">."""
    return json.dumps(data).translate(_SCRIPT_BREAKOUT_ESCAPES)


def breadcrumb_list_schema(items):
    """items: list of (name, url_or_None) tuples. Last item is typically
    the current page, so its url can be None (schema.org allows a
    ListItem without an `item` URL for the final entry)."""
    return safe_json_dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                **({"item": url} if url else {}),
            }
            for i, (name, url) in enumerate(items)
        ],
    })


def service_schema(service, request):
    return safe_json_dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": service.name,
        "description": service.short_description,
        "provider": {"@type": "ProfessionalService", "name": "Luminous Ever"},
        "url": request.build_absolute_uri(service.get_absolute_url()),
    })
