from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', 'mutual_funds', 'term_deposit', 'life_insurance']

    def location(self, item):
        return reverse(item)
