"""
Sitemap classes for /sitemap.xml. Centralized here rather than scattered
per-app — reasonable for a project this size, and keeps the full list of
indexable URLs visible in one place.
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import BlogPost
from apps.portfolio.models import CaseStudy
from apps.services.models import Industry, Service


class StaticViewSitemap(Sitemap):
    """Fixed pages that aren't backed by a per-object model."""

    def items(self):
        return [
            ("core:home", 1.0, "weekly"),
            ("core:about", 0.6, "monthly"),
            ("team:index", 0.5, "monthly"),
            ("services:index", 0.8, "weekly"),
            ("services:industries", 0.6, "monthly"),
            ("portfolio:index", 0.8, "weekly"),
            ("blog:index", 0.7, "weekly"),
            ("faq:index", 0.5, "monthly"),
            ("leads:contact", 0.8, "monthly"),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class IndustrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Industry.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class CaseStudySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return CaseStudy.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
    "industries": IndustrySitemap,
    "portfolio": CaseStudySitemap,
    "blog": BlogPostSitemap,
}
