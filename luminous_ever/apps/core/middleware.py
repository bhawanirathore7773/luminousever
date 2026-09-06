class UTMTrackingMiddleware:
    """
    Captures utm_source / utm_medium / utm_campaign (and the landing page)
    from the querystring on first touch and persists them in the session so
    the leads app can attribute a submission days later, regardless of which
    page the form was actually filled out on.
    """

    UTM_PARAMS = ["utm_source", "utm_medium", "utm_campaign"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if any(param in request.GET for param in self.UTM_PARAMS):
            for param in self.UTM_PARAMS:
                if param in request.GET:
                    request.session[param] = request.GET[param]
            request.session.setdefault("landing_page", request.path)

        return self.get_response(request)


class ContentSecurityPolicyMiddleware:
    """
    Adds a Content-Security-Policy header restricting external resource
    origins to the specific CDNs this site actually uses (Google Fonts,
    unpkg for Lenis, cdnjs for GSAP) rather than leaving script/style/font/
    connect wide open.

    Honest trade-off, documented rather than hidden: script-src and
    style-src both need 'unsafe-inline' here. The site uses inline
    style="" attributes extensively (a deliberate, pragmatic choice
    throughout this build — see components.css comments) and inline
    <script type="application/ld+json"> blocks for structured data: a
    nonce- or hash-based CSP strict enough to drop 'unsafe-inline' would
    mean threading a nonce through every template and is real, separate
    work — not something to bolt on silently in a security pass. What
    this CSP *does* still block: arbitrary third-party scripts/styles/
    frames from origins outside this explicit allowlist, which is the
    main real-world threat (injected/exfiltrating scripts) a CSP defends
    against. Tightening further is a good follow-up once there's a real
    browser available to verify nothing silently breaks — that can't be
    confirmed from server-side tests alone.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.policy = "; ".join([
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://unpkg.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net",
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
            "font-src 'self' https://fonts.gstatic.com",
            "img-src 'self' data: https:",
            "connect-src 'self'",
            "frame-src https://www.google.com",  # Google Maps embed on the contact page
            "object-src 'none'",
            "base-uri 'self'",
            "form-action 'self'",
            "frame-ancestors 'none'",
        ])

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", self.policy)
        return response
