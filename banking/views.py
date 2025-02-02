import io

from django.core.files.base import ContentFile
from django.db.models import Q, FloatField, F, ExpressionWrapper
from django.shortcuts import redirect, render
from pdf2image import convert_from_bytes
from django import template
from django.http import JsonResponse

from .models import BankProduct, Investment



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
    # Fetch all banks and available product choices
    banks = BankProduct.objects.all()
    products = Investment.PRODUCT_CHOICES
    investments = Investment.objects.filter(investment_type='local')

    # Fetch distinct filter values
    bank_filter_names = investments.values_list('bank__bank_name', flat=True).distinct()
    bank_filter = [{'bank_name': name} for name in bank_filter_names]
    payout_frequencies = investments.values_list('payout_frequency', flat=True).distinct()

    # Convert choice_field keys to display names
    period_choices_dict = dict(Investment.PRODUCT_CHOICES)
    period_keys = investments.values_list('choice_field', flat=True).distinct()
    period_display_names = [period_choices_dict.get(key, key) for key in period_keys]

    # Read query parameters
    selected_frequency = request.GET.get('payout_frequency', '')
    selected_period = request.GET.get('period', '')
    selected_bank = request.GET.get('bank', '')

    # Apply filters based on query parameters
    filtered_investments = investments
    if selected_frequency:
        filtered_investments = filtered_investments.filter(payout_frequency=selected_frequency)
    if selected_period:
        period_key = {v: k for k, v in period_choices_dict.items()}.get(selected_period)
        if period_key:
            filtered_investments = filtered_investments.filter(choice_field=period_key)
    if selected_bank:
        filtered_investments = filtered_investments.filter(bank__bank_name=selected_bank)

    # Exclude invalid profit rates (non-numeric, disclosed, or negative values)
    filtered_investments = filtered_investments.exclude(
        Q(profit_rate__contains='disclosed') |
        Q(profit_rate__contains='-') |
        Q(profit_rate__contains=' ') |
        Q(profit_rate__isnull=True)
    )

    # Convert profit_rate to float for correct numerical sorting
    filtered_investments = filtered_investments.annotate(
        profit_rate_numeric=ExpressionWrapper(F('profit_rate'), output_field=FloatField())
    )

    # Sort by profit rate in descending order and get top 5 products
    top_products = filtered_investments.order_by('-profit_rate_numeric')[:5]

    # Default top 5 products when no filters are applied
    if not (selected_frequency or selected_period or selected_bank):
        default_investments = Investment.objects.filter(investment_type='local').exclude(
            Q(profit_rate__contains='disclosed') |
            Q(profit_rate__contains='-') |
            Q(profit_rate__contains=' ') |
            Q(profit_rate__isnull=True)
        ).annotate(
            profit_rate_numeric=ExpressionWrapper(F('profit_rate'), output_field=FloatField())
        ).order_by('-profit_rate_numeric')[:5]
        top_products = default_investments

    # Handle AJAX request and return the filtered products as JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        top_products_data = [
            {
                'bank_name': product.bank.bank_name,
                'bank_image': product.bank.bank_image.url if product.bank.bank_image else None,
                'product_length': product.product_length,
                'profit_rate': product.profit_rate,
                'payout_frequency': product.payout_frequency,
                'period': period_choices_dict.get(product.choice_field, ''),
                'currency': product.currency,
                'min_investment': product.min_investment,
                'max_investment': product.max_investment,
                'rating_long_term': product.rating_long_term,
                'rating_short_term': product.rating_short_term,
            }
            for product in top_products
        ]
        return JsonResponse({'top_products': top_products_data})

    # Context for template rendering
    context = {
        'banks': banks,
        'products': products,
        'investments': investments,
        'top_products': top_products,
        'payout_frequencies': payout_frequencies,
        'periods': period_display_names,
        'bank_filter': bank_filter,
    }

    return render(request, 'products.html', context)

def foreign_investment_list(request):
    # Fetch all banks for the dropdown
    banks = BankProduct.objects.all()
    products = Investment.PRODUCT_CHOICES
    investments = Investment.objects.filter(investment_type='foreign')

    # Filter dropdown data
    bank_filter_names = investments.values_list('bank__bank_name', flat=True).distinct()
    bank_filter = [{'bank_name': name} for name in bank_filter_names]
    payout_frequencies = investments.values_list('payout_frequency', flat=True).distinct()
    period_keys = investments.values_list('choice_field', flat=True).distinct()
    period_display_names = [dict(Investment.PRODUCT_CHOICES)[key] for key in period_keys]
    FOREIGN_CURRENCY_CHOICES = investments.values_list('currency', flat=True).distinct()

    # Read filter values from query parameters
    selected_frequency = request.GET.get('payout_frequency', '')
    selected_period = request.GET.get('period', '')
    selected_currency = request.GET.get('currency', '')

    # Filter investments based on query parameters
    filtered_investments = investments
    if selected_frequency:
        filtered_investments = filtered_investments.filter(payout_frequency=selected_frequency)
    if selected_period:
        # Convert period display name back to the key
        period_key = next(
            (key for key, value in Investment.PRODUCT_CHOICES if value == selected_period), None
        )
        if period_key:
            filtered_investments = filtered_investments.filter(choice_field=period_key)
    if selected_currency:
        filtered_investments = filtered_investments.filter(currency=selected_currency)

    # Get top 5 products based on filtered investments
    top_products = filtered_investments.exclude(
        Q(profit_rate__contains='disclosed') | Q(profit_rate__contains='-') | Q(profit_rate__contains=' ')
    ).order_by('-profit_rate')[:5]

    # Check for AJAX request (to update top products dynamically)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        top_products_data = [
            {
                'bank_name': product.bank.bank_name,
                'bank_image': product.bank.bank_image.url if product.bank.bank_image else None,
                'product_length': product.product_length,
                'currency': product.currency,
                'profit_rate': product.profit_rate,
                'min_investment': product.min_investment,
                'max_investment': product.max_investment,
                'payout_frequency': product.payout_frequency,
                'period': dict(Investment.PRODUCT_CHOICES)[product.choice_field],
                'rating_long_term': product.rating_long_term,
                'rating_short_term': product.rating_short_term,
            }
            for product in top_products
        ]
        return JsonResponse({'top_products': top_products_data})

    context = {
        'banks': banks,
        'products': products,
        'investments': investments,
        'top_products': top_products,
        'payout_frequencies': payout_frequencies,
        'periods': period_display_names,
        'bank_filter': bank_filter,
        'foreign_currency_choices': FOREIGN_CURRENCY_CHOICES,
    }

    return render(request, 'foreign_products.html', context)


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
    return render(request, 'calculators_template.html')


def quarterly(request):
    return render(request, 'quarterly_template.html')


def monthly(request):
    return render(request, 'monthly_template.html')


def biannual(request):
    return render(request, 'biannual_template.html')


def recurring(request):
    return render(request, 'recurring_template.html')


def ruleof72(request):
    return render(request, 'rule_of_72_template.html')

def ruleof78(request):
    return render(request, 'rule_of_78_template.html')


def mutualfundcalculator(request):
    return render(request, 'mutualfundcalculator_template.html')


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
    subsidiary_of = funds.values_list('subsidiary_of', flat=True).distinct()
    # Extracting additional columns from ytd_as_of_date
    additional_columns = set()
    # for fund in funds:
    #     if fund.ytd_as_of_date:
    #         additional_columns.update(fund.ytd_as_of_date.keys())

    for fund in funds:
        if fund.performance:
            fund.performance = fund.performance.replace(',', ',<br>').replace(':', ':<br>').replace(';', ';<br>')
    
    

    context = {
        'funds': funds,
        'additional_columns': sorted(additional_columns),
        'subsidiary_of': subsidiary_of
    }
    return render(request, 'islamic.html', context)


def conventional(request):
    funds = ConventionalFund.objects.all()
    # Extracting additional columns from ytd_as_of_date
    subsidiary_of = funds.values_list('subsidiary_of', flat=True).distinct()
    additional_columns = set()
    # for fund in funds:
    #     if fund.ytd_as_of_date:
    #         additional_columns.update(fund.ytd_as_of_date.keys())

    for fund in funds:
        if fund.performance:
            fund.performance = fund.performance.replace(',', ',<br>').replace(':', ':<br>').replace(';', ';<br>')
    
    context = {
        'funds': funds,
        'additional_columns': sorted(additional_columns),
        'subsidiary_of': subsidiary_of
    }
    return render(request, 'conventional.html', context)
