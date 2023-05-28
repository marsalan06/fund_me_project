from django.contrib import admin
from .models import Bank, Product

# Register your models here.

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'branches', 'date_of_operation')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','bank', 'minimum_balance', 'indicative_rate', 'profit_payout_freq', 'earning_per_1000', 'premature_fee')

    def display_indicative_rate(self, obj):
        return f"{obj.indicative_rate}%"

    display_indicative_rate.short_description = 'Indicative Rate'
