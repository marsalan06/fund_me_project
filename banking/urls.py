from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mutualfunds/', views.mutual_funds, name='mutualfunds'),
    path('calculator/', views.calculator, name='calculator')

    # Add more URL patterns here if needed
]