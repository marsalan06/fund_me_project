from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from banking.views import robots_txt  # make sure this view is implemented
from banking.sitemap import StaticViewSitemap  # create this file if not already

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('banking.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
