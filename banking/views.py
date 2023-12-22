from django.shortcuts import render

from .models import (BankProduct, InsuranceProduct, Investment,
                     LifeInsuranceCompany)

# Create your views here.


def home(request):
    return render(request, 'index.html')


def mutual_funds(request):
    return render(request, 'mutual_funds.html')


def calculator(request):
    return render(request, 'calculator.html')


def islamic(request):
    return render(request, 'islamic.html')


def conventional(request):
    return render(request, 'conventional.html')


def term_deposites(request):
    return render(request, 'term_deposite.html')


def faqs(request):
    return render(request, 'faqs.html')


def investment_list(request):
    # Fetch all banks for the dropdown

    banks = BankProduct.objects.all()
    products = Investment.PRODUCT_CHOICES
    investments = Investment.objects.all()
    context = {
        'banks': banks,
        'products': products,
        'investments': investments,
    }

    return render(request, 'products.html', context)


def life_insurance(request):
    return render(request, 'life_insurance.html')


def life_insurance_companies(request):
    return render(request, 'life_insurance_companies.html')


def mutual_fund_companies(request):
    return render(request, 'mutual_funds_companies.html')


def life_insurance_products(request):
    # Fetch all banks for the dropdown

    life_insurance_companies = LifeInsuranceCompany.objects.all()
    frequency = InsuranceProduct.FREQUENCY_CHOICES
    insurance_products = InsuranceProduct.objects.all()
    context = {
        'life_insurance_companies': life_insurance_companies,
        'frequency': frequency,
        'insurance_products': insurance_products,
    }
    return render(request, 'life_insurance_products.html', context)


def future_value_calculator(request):
    return render(request, 'future_value_calculator.html')
