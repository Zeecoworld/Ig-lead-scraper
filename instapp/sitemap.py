from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse



class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home','contact-us']

    def location(self, item):
        return reverse(item)
