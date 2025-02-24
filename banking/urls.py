from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mutualfunds/', views.mutual_funds, name='mutualfunds'),
    path('calculator/', views.calculator, name='calculator'),
    path('islamic/', views.islamic, name='islamic'),
    path('conventional/', views.conventional, name='conventional'),
    path('term-deposits/', views.term_deposites, name='term_deposites'),
    path('faq/', views.faqs, name='faqs'),
    path('products/', views.investment_list, name='investment_list'),
    path('foreign/', views.foreign_investment_list, name='foreign_currency'),
    path('life-insurance/', views.life_insurance, name='life_insurance'),
    path('life-insurance-companies/', views.life_insurance_companies,
         name='life_insurance_companies'),
    path('mutual-fund-companies/', views.mutual_fund_companies,
         name='mutual_fund_companies'),
    path('life-insurance-products/', views.life_insurance_products,
         name='life_insurance_list'),
    path('future_value_calculator/', views.future_value_calculator,
         name='future_value_calculator'),
    path('calculators/', views.calculators,
         name='calculators'),
    path('quarterly/', views.quarterly,
         name='quarterly'),
    path('monthly/', views.monthly,
         name='monthly'),
    path('biannual/', views.biannual,
         name='biannual'),
    path('recurring/', views.recurring,
         name='recurring'),
    path('ruleof72/', views.ruleof72,
         name='ruleof72'),
    path('ruleof78/', views.ruleof78,
         name='ruleof78'),
    path('mutualfundcalculator/', views.mutualfundcalculator,
         name='mutualfundcalculator'),
    path('article/', views.upload_article, name='upload_article'),

    # Add more URL patterns here if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
