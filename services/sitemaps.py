from django.contrib.sitemaps import Sitemap
from .models import AttractionCategory, Attraction
from django.shortcuts import reverse
from .models import Snippet

class AttractionCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return AttractionCategory.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)

class AttractionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Attraction.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_date

    def location(self,obj):
        return '/%s' % (obj.slug)

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['home', 'gallery']

    def location(self, item):
        return reverse(item)
#========= sitemap snippet===================
class SnippetSitemap(Sitemap):
    def items(self):
        return Snippet.objects.all()
