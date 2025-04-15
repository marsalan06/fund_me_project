# banking/sitemap.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return [
            'home', 'mutualfunds', 'calculator', 'islamic', 'conventional', 'term_deposites', 'faqs',
            'investment_list', 'foreign_currency', 'life_insurance', 'life_insurance_companies', 
            'mutual_fund_companies', 'life_insurance_list', 'future_value_calculator', 'calculators',
            'quarterly', 'monthly', 'biannual', 'recurring', 'ruleof72', 'ruleof78', 'mutualfundcalculator', 'upload_article'
        ]

    def location(self, item):
        return reverse(item)
