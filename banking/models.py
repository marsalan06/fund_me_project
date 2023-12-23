from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, default=None)
    branches = models.PositiveIntegerField(default=1)
    date_of_operation = models.DateField(default=None)

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
    # Add your specific choices here

    def __str__(self):
        return self.bank_name


class Investment(models.Model):

    PRODUCT_CHOICES = [
        ('short_term', 'Short Notice Term Deposit Certificate'),
        ('one_month', 'One Month Deposite Certificate'),
        ('three_month', 'Three Months Term Deposite Certificate'),
        ('six_month', 'Six Months Term Deposite Certificate'),
        ('one_year', 'One Year Term Deposite Certificate'),
        ('three_year', 'Three Year Term Deposite Certificate'),
        ('five_year', 'Five Year Term Deposite Certificate'),
        ('month_quarter_half', 'Monthly / Quaterly / Half Yearly Term Deposite Certificate'),
        ('ten_year', 'Ten Year Term Deposite Certificate'),
        ('recurring', 'Monthly Recurring Deposite Certificate')
        # Add more banks as needed
    ]

    bank = models.ForeignKey(BankProduct, on_delete=models.CASCADE)
    min_investment = models.DecimalField(max_digits=12, decimal_places=2)
    max_investment = models.DecimalField(max_digits=12, decimal_places=2)
    product_length = models.CharField(max_length=100)
    rating_short_term = models.CharField(max_length=10, null=True)
    rating_long_term = models.CharField(max_length=10, null=True)
    profit_rate = models.CharField(max_length=100)
    payout_frequency = models.CharField(max_length=50)
    choice_field = models.CharField(
        max_length=50, choices=PRODUCT_CHOICES, null=False, default=PRODUCT_CHOICES[0])

    def __str__(self):
        return f"{self.bank.bank_name} - {self.product_length}"


class LifeInsuranceCompany(models.Model):

    company_name = models.CharField(max_length=100, null=False, unique=True)
    # Add your specific choices here

    def __str__(self):
        return self.company_name


class InsuranceProduct(models.Model):
    FREQUENCY_CHOICES = [
        ('yearly', 'Yearly'),
        ('half_yearly', 'Half Yearly'),
        ('quarterly', 'Quarterly'),
        ('monthly', 'Monthly'),
    ]

    company = models.ForeignKey(LifeInsuranceCompany, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, null=True, blank=True)
    min_eligibility_age = models.IntegerField()
    max_eligibility_age = models.IntegerField()
    max_maturity_age = models.BooleanField(default=False)
    minimum_premium = models.DecimalField(max_digits=12, decimal_places=2)
    product_length = models.CharField(max_length=100, null=True, blank=True)
    min_policy_term = models.CharField(max_length=100, null=True, blank=True)
    max_policy_term = models.CharField(max_length=100, null=True, blank=True)
    contribution_allocation = models.CharField(
        max_length=100, null=True, blank=True)
    premium_frequency = models.CharField(
        max_length=20, choices=FREQUENCY_CHOICES, null=False)
    loan_against_premium_paid = models.CharField(
        max_length=100, null=True, blank=True)
    free_look_up_period = models.CharField(
        max_length=10, null=True, blank=True)
    partial_full_withdrawal = models.CharField(
        max_length=100, null=True, blank=True)
    inflation_protection = models.CharField(
        max_length=100, null=True, blank=True)
    charges = models.CharField(max_length=255, null=True, blank=True)
    bonus_allocation = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_1 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_2 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_3 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_4 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_5 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_6 = models.CharField(max_length=100, null=True, blank=True)
    product_benefit_7 = models.CharField(max_length=100, null=True, blank=True)
    optional_benefits = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.company.company_name} - {self.id}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    preview_image = models.ImageField(
        upload_to='previews/', null=True, blank=True)

    def __str__(self):
        return self.title
