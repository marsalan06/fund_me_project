from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mutualfunds/', views.mutual_funds, name='mutualfunds'),
    path('calculator/', views.calculator, name='calculator'),
    path('islamic/', views.islamic, name='islamic'),
    path('conventional/', views.conventional, name='conventional'),
    path('term-deposite/', views.term_deposites, name='term_deposites'),
    path('faq/', views.faqs, name='faqs'),
    path('products/', views.investment_list, name='investment_list')


    # Add more URL patterns here if needed
]
