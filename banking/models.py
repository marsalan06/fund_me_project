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
    profit_payout_freq_choices = (
        ('D', 'Daily'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('BA', 'Biannually'),
        ('A', 'Annually'),
        ('MA', 'Maturity'),
    )
    profit_payout_freq = models.CharField(max_length=2, choices=profit_payout_freq_choices)
    earning_per_1000_lower_limit = models.DecimalField(max_digits=10, decimal_places=2)
    earning_per_1000_upper_limit = models.DecimalField(max_digits=10, decimal_places=2)
    premature_encashment = models.CharField(max_length=100)

    def __str__(self):
        return f"Product {self.id} - Bank: {self.bank.name}"