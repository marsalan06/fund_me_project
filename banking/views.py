import io

from django.core.files.base import ContentFile
from django.shortcuts import redirect, render
from pdf2image import convert_from_bytes
from django.db.models import Q


from .forms import ArticleForm
from .models import (Article, BankProduct, ConventionalFund, InsuranceProduct,
                     Investment, IslamicFund, LifeInsuranceCompany)

# Create your views here.


def home(request):
    return render(request, 'index.html')


def mutual_funds(request):
    return render(request, 'mutual_funds.html')


def calculator(request):
    return render(request, 'calculator.html')


# def islamic(request):
#     return render(request, 'islamic.html')


# def conventional(request):
#     return render(request, 'conventional.html')


def term_deposites(request):
    return render(request, 'term_deposite.html')


def faqs(request):
    return render(request, 'faqs.html')


def investment_list(request):
    # Fetch all banks for the dropdown

    banks = BankProduct.objects.all()
    products = Investment.PRODUCT_CHOICES
    investments = Investment.objects.all()
    top_products = Investment.objects.exclude(
        Q(profit_rate__contains='disclosed') | Q(profit_rate__contains='-') | Q(profit_rate__contains=' ')
    ).order_by('-profit_rate')[:5]    
    context = {
        'banks': banks,
        'products': products,
        'investments': investments,
        'top_products': top_products,
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

def calculators(request):
    return render(request, 'calculators.html')

def quarterly(request):
    return render(request, 'quarterly.html')


def monthly(request):
    return render(request, 'monthly.html')

def biannual(request):
    return render(request, 'biannual.html')


def recurring(request):
    return render(request, 'recurring.html')

def mutualfundcalculator(request):
    return render(request, 'mutualfundcalculator.html')

def upload_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)

            # Handle PDF preview generation
            pdf = request.FILES['pdf']
            pdf_bytes = pdf.read()

            # Convert the first page of the PDF to an image
            images = convert_from_bytes(pdf_bytes, first_page=1, last_page=1)
            if images:
                # Convert the first image to a JPEG
                image_io = io.BytesIO()
                images[0].save(image_io, format='JPEG', quality=85)
                image_io.seek(0)
                article.preview_image.save(
                    f'preview_{article.title}.jpg', ContentFile(image_io.getvalue()), save=False)

            article.save()
            return redirect('upload_article')
    else:
        form = ArticleForm()

    articles = Article.objects.all()
    return render(request, 'article.html', {'form': form, 'articles': articles})


def islamic(request):
    funds = IslamicFund.objects.all()
    # Extracting additional columns from ytd_as_of_date
    additional_columns = set()
    for fund in funds:
        if fund.ytd_as_of_date:
            additional_columns.update(fund.ytd_as_of_date.keys())

    context = {
        'funds': funds,
        'additional_columns': sorted(additional_columns)
    }
    return render(request, 'islamic.html', context)


def conventional(request):
    funds = ConventionalFund.objects.all()
    # Extracting additional columns from ytd_as_of_date
    additional_columns = set()
    for fund in funds:
        if fund.ytd_as_of_date:
            additional_columns.update(fund.ytd_as_of_date.keys())

    context = {
        'funds': funds,
        'additional_columns': sorted(additional_columns)
    }
    return render(request, 'conventional.html', context)
