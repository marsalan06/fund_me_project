from django.db import models
from django.shortcuts import render

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, default=None)
    branches = models.PositiveIntegerField(default=1)
    date_of_operation = models.DateField(default=None)
    bank_image = models.ImageField(upload_to='bank_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    minimum_balance = models.DecimalField(max_digits=10, decimal_places=2)
    rate_lower_limit = models.DecimalField(max_digits=5, decimal_places=2)
    rate_upper_limit = models.DecimalField(max_digits=5, decimal_places=2)

    OCCURRENCES_PER_YEAR = {
        'D': 365,
        'M': 12,
        'Q': 4,
        'BA': 2,
        'A': 1,
        'MA': 1,  # Assuming Maturity has no specific occurrence per year
    }

    profit_payout_freq_choices = (
        ('D', 'Daily'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('BA', 'Biannually'),
        ('A', 'Annually'),
        ('MA', 'Maturity'),
    )
    profit_payout_freq = models.CharField(
        max_length=2, choices=profit_payout_freq_choices)

    earning_per_1000_lower_limit = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    earning_per_1000_upper_limit = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    premature_encashment = models.CharField(max_length=100)

    def calculate_earning_per_1000_limits(self):
        # Perform your calculation here
        occurrences_per_year = self.OCCURRENCES_PER_YEAR[self.profit_payout_freq]
        # earning_per_1000_lower_limit = self.minimum_balance * (self.rate_lower_limit / 1000) * occurrences_per_year
        # earning_per_1000_upper_limit = self.minimum_balance * (self.rate_upper_limit / 1000) * occurrences_per_year

        earning_per_1000_lower_limit = 1000 * \
            (self.rate_lower_limit/occurrences_per_year)
        earning_per_1000_upper_limit = 1000 * \
            (self.rate_upper_limit/occurrences_per_year)

        return earning_per_1000_lower_limit, earning_per_1000_upper_limit

    def save(self, *args, **kwargs):
        # New instance, calculate the limits
        earning_per_1000_lower_limit, earning_per_1000_upper_limit = self.calculate_earning_per_1000_limits()
        self.earning_per_1000_lower_limit = earning_per_1000_lower_limit
        self.earning_per_1000_upper_limit = earning_per_1000_upper_limit

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product {self.id} - Bank: {self.bank.name}"


class BankProduct(models.Model):

    bank_name = models.CharField(max_length=100, null=False, unique=True)
    bank_image = models.ImageField(upload_to='bank_images/', null=True, blank=True)

    def __str__(self):
        return self.bank_name


from django.core.exceptions import ValidationError
from django.db import models

from django.core.exceptions import ValidationError
from django.db import models

from django.core.exceptions import ValidationError
from django.db import models

class Investment(models.Model):

    PRODUCT_CHOICES = [
        ('short_term', 'Short Notice Term Deposit Certificate'),
        ('one_month', 'One Month Deposit Certificate'),
        ('three_month', 'Three Months Term Deposit Certificate'),
        ('six_month', 'Six Months Term Deposit Certificate'),
        ('one_year', 'One Year Term Deposit Certificate'),
        ('three_year', 'Three Year Term Deposit Certificate'),
        ('five_year', 'Five Year Term Deposit Certificate'),
        ('month_quarter_half', 'Monthly / Quaterly / Half Yearly Term Deposit Certificate'),
        ('ten_year', 'Ten Year Term Deposit Certificate'),
        ('recurring', 'Monthly Recurring Deposit Certificate'),
    ]

    INVESTMENT_TYPE_CHOICES = [
        ('local', 'Local'),
        ('foreign', 'Foreign'),
    ]

    CURRENCY_CHOICES = [
        ('PKR', 'PKR'),
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
        ('AED', 'AED'),
        ('SAR', 'SAR'),
    ]

    # MAX_INVESTMENT_CHOICES = [
    #     ('mention_amount', 'Mention the Amount'),
    #     ('no_limit', 'No Limit'),
    #     ('amount_above', 'Amount in Figure & Above'),
    # ]

    bank = models.ForeignKey('BankProduct', on_delete=models.CASCADE)
    # min_investment = models.DecimalField(max_digits=12, decimal_places=2)
    # max_investment_type = models.CharField(
    #     max_length=20, choices=MAX_INVESTMENT_CHOICES, null=False, default='mention_amount')
    # max_investment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    min_investment = models.CharField(max_length=100, null=True)
    max_investment = models.CharField(max_length=100, null=True)
    product_length = models.CharField(max_length=100)
    rating_short_term = models.CharField(max_length=10, null=True)
    rating_long_term = models.CharField(max_length=10, null=True)
    # is_expected_profit_rate = models.BooleanField(default=False)
    profit_rate = models.CharField(max_length=100)
    payout_frequency = models.CharField(max_length=50)
    choice_field = models.CharField(
        max_length=50, choices=PRODUCT_CHOICES, null=False, default=PRODUCT_CHOICES[0][0])
    investment_type = models.CharField(
        max_length=50, choices=INVESTMENT_TYPE_CHOICES, null=False, default=INVESTMENT_TYPE_CHOICES[0][0])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = "Term Deposit"
        verbose_name_plural = "Term Deposits"

    def clean(self):
        """Validate currency choices and enforce PKR for local investments."""
        if self.investment_type == 'local':
            # Force currency to PKR for local investments
            if self.currency != 'PKR':
                raise ValidationError("Local investments must have PKR as the currency.")
        elif self.investment_type == 'foreign':
            # Ensure PKR is not selected for foreign investments
            if self.currency == 'PKR':
                raise ValidationError("PKR cannot be selected for foreign investments.")
            if self.currency not in dict(self.CURRENCY_CHOICES):
                raise ValidationError(f"Invalid currency. Must be one of: {', '.join(dict(self.CURRENCY_CHOICES).keys())}.")

        # Validate max investment based on the selected type
        # if self.max_investment_type == 'mention_amount' and not self.max_investment:
        #     raise ValidationError("Maximum investment amount must be specified when 'Mention the Amount' is selected.")
        # if self.max_investment_type == 'no_limit' and self.max_investment:
        #     raise ValidationError("Maximum investment amount should not be specified when 'No Limit' is selected.")
        # if self.max_investment_type == 'amount_above' and not self.max_investment:
        #     raise ValidationError("Maximum investment base amount must be specified for 'Amount in Figure & Above'.")

    def save(self, *args, **kwargs):
        # Auto-assign PKR for local investments before saving
        if self.investment_type == 'local':
            self.currency = 'PKR'
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bank.bank_name} - {self.product_length}"





class LifeInsuranceCompany(models.Model):

    company_name = models.CharField(max_length=100, null=False, unique=True)
    company_image = models.ImageField(upload_to='company_images/', null=True, blank=True)


    def __str__(self):
        return self.company_name

class InsuranceProduct(models.Model):
    FREQUENCY_CHOICES = [
        ('yearly', 'Yearly'),
        ('half_yearly', 'Half Yearly'),
        ('quarterly', 'Quarterly'),
        ('monthly', 'Monthly'),
    ]

    company = models.ForeignKey(LifeInsuranceCompany, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    min_eligibility_age = models.IntegerField(null=True, blank=True)
    max_eligibility_age = models.IntegerField(null=True, blank=True)
    max_maturity_age = models.IntegerField(null=True, blank=True)
    minimum_premium = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    product_length = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    min_policy_term = models.CharField(max_length=100, null=True, blank=True)
    max_policy_term = models.CharField(max_length=100, null=True, blank=True)
    contribution_allocation = models.CharField(max_length=100, null=True, blank=True)
    premium_frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, null=True, blank=True)
    loan_against_premium_paid = models.CharField(max_length=100, null=True, blank=True)
    free_look_up_period = models.CharField(max_length=10, null=True, blank=True)
    partial_full_withdrawal = models.CharField(max_length=100, null=True, blank=True)
    inflation_protection = models.CharField(max_length=100, null=True, blank=True)
    charges = models.CharField(max_length=255, null=True, blank=True)
    bonus_allocation = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_1 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_2 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_3 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_4 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_5 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_6 = models.CharField(max_length=200, null=True, blank=True)
    product_benefit_7 = models.CharField(max_length=200, null=True, blank=True)
    optional_benefits = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.company.company_name if self.company else 'No Company'} - {self.id}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    preview_image = models.ImageField(
        upload_to='previews/',blank=False, null=False)

    def __str__(self):
        return self.title


class IslamicFund(models.Model):
    asset_management_company = models.CharField(max_length=100, null=True, blank=True)
    subsidiary_of = models.CharField(max_length=100, null=True)  # Subsidiary of
    fund_name = models.CharField(max_length=100, null=True)  # Fund Name
    launch_date = models.CharField(max_length=100, null=True)   # Launch Date
    fund_size = models.CharField(max_length=20, null=True)  # Fund Size
    fund_type = models.CharField(max_length=50, null=True)  # Fund Type
    rating = models.CharField(max_length=10, null=True)  # Rating
    risk = models.CharField(max_length=50, null=True)  # Risk
    minimum_investment_in_pkr = models.CharField(max_length=50, null=True)  # Minimum Investment
    performance = models.TextField(null=True)  # Performance in the past 3 years (%)
    ytd_as_of = models.CharField(max_length=100, null=True)  # Return as of Last Month
    front_back_end_load = models.CharField(max_length=50, null=True)  # Front & Back-end Loading
    # back_end_load = models.CharField(max_length=50)  # Back-end Loading
    management_fee = models.CharField(max_length=50, null=True)  # Management Fee

    def __str__(self):
        return self.fund_name


class ConventionalFund(models.Model):
    asset_management_company = models.CharField(max_length=100, null=True, blank=True)
    subsidiary_of = models.CharField(max_length=100, null=True)  # Subsidiary of
    fund_name = models.CharField(max_length=100, null=True)  # Fund Name
    launch_date = models.CharField(max_length=100, null=True)   # Launch Date
    fund_size = models.CharField(max_length=20, null=True)  # Fund Size
    fund_type = models.CharField(max_length=50, null=True)  # Fund Type
    rating = models.CharField(max_length=10, null=True)  # Rating
    risk = models.CharField(max_length=50, null=True)  # Risk
    minimum_investment_in_pkr = models.CharField(max_length=50, null=True)  # Minimum Investment
    performance = models.TextField(null=True)  # Performance in the past 3 years (%)
    ytd_as_of = models.CharField(max_length=100, null=True)  # Return as of Last Month
    front_back_end_load = models.CharField(max_length=50, null=True)  # Front & Back-end Loading
    # back_end_load = models.CharField(max_length=50)  # Back-end Loading
    management_fee = models.CharField(max_length=50, null=True)  # Management Feedef __str__(self):
    
    
    def __str__(self):
        return self.fund_name