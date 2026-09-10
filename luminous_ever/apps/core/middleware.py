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
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.policy = "; ".join([
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://unpkg.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net",
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
            "font-src 'self' https://fonts.gstatic.com",
            "img-src 'self' data: https:",
            "connect-src 'self' https://unpkg.com https://cdnjs.cloudflare.com",
            "frame-src https://www.google.com",
            "object-src 'none'",
            "base-uri 'self'",
            "form-action 'self'",
            "frame-ancestors 'none'",
        ])

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", self.policy)
        return response
