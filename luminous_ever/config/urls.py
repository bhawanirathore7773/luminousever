"""
Root URL configuration for Luminous Ever.

Every top-level destination the navbar/footer link to resolves to a real
view — the entire site is live as of Phase 9. /sitemap.xml and /robots.txt
(Phase 10) round out the crawlable surface.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.core.views import robots_txt
from config.sitemaps import sitemaps

urlpatterns = [
    path(settings.ADMIN_URL_PATH, admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("", include("apps.services.urls", namespace="services")),
    path("", include("apps.portfolio.urls", namespace="portfolio")),
    path("", include("apps.blog.urls", namespace="blog")),
    path("", include("apps.leads.urls", namespace="leads")),
    path("", include("apps.team.urls", namespace="team")),
    path("", include("apps.faq.urls", namespace="faq")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", robots_txt, name="robots_txt"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
