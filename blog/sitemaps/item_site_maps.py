from django.contrib.sitemaps import Sitemap

from blog.models import Tag


class ItemSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Tag.objects.filter()

    def lastmod(self, obj):
        return obj.updated_at