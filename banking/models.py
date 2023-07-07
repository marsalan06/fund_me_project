from django.db import models

# Create your models here.


from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, default=None)
    branches = models.PositiveIntegerField(default=1)
    date_of_operation = models.DateField(default=None)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
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
    profit_payout_freq = models.CharField(max_length=2, choices=profit_payout_freq_choices)

    earning_per_1000_lower_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    earning_per_1000_upper_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    premature_encashment = models.CharField(max_length=100)

    def calculate_earning_per_1000_limits(self):
        # Perform your calculation here
        occurrences_per_year = self.OCCURRENCES_PER_YEAR[self.profit_payout_freq]
        # earning_per_1000_lower_limit = self.minimum_balance * (self.rate_lower_limit / 1000) * occurrences_per_year
        # earning_per_1000_upper_limit = self.minimum_balance * (self.rate_upper_limit / 1000) * occurrences_per_year
        
        earning_per_1000_lower_limit = 1000 * (self.rate_lower_limit/occurrences_per_year)
        earning_per_1000_upper_limit = 1000 * (self.rate_upper_limit/occurrences_per_year)

        return earning_per_1000_lower_limit, earning_per_1000_upper_limit

    def save(self, *args, **kwargs):
        # New instance, calculate the limits
        earning_per_1000_lower_limit, earning_per_1000_upper_limit = self.calculate_earning_per_1000_limits()
        self.earning_per_1000_lower_limit = earning_per_1000_lower_limit
        self.earning_per_1000_upper_limit = earning_per_1000_upper_limit

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Product {self.id} - Bank: {self.bank.name}"