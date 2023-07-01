from django.contrib import admin
from .models import Bank, Product

# Register your models here.

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'branches', 'date_of_operation')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','bank', 'minimum_balance', 'rate_lower_limit', 'rate_upper_limit', 'profit_payout_freq', 'earning_per_1000_lower_limit', 'earning_per_1000_upper_limit', 'premature_encashment')
    list_filter = ('bank','profit_payout_freq','rate_lower_limit','rate_upper_limit')
    def display_indicative_rate(self, obj):
        return f"{obj.indicative_rate}%"

    display_indicative_rate.short_description = 'Indicative Rate'
