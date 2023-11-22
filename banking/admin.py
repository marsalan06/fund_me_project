import csv

import pandas as pd
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from .models import Bank, BankProduct, Investment, Product

# Register your models here.


# @admin.register(Bank)
# class BankAdmin(admin.ModelAdmin):
#     list_display = ('name', 'rating', 'branches', 'date_of_operation')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'bank', 'minimum_balance', 'rate_lower_limit', 'rate_upper_limit', 'profit_payout_freq',
#                     'earning_per_1000_lower_limit', 'earning_per_1000_upper_limit', 'premature_encashment')
#     list_filter = ('bank', 'profit_payout_freq',
#                    'rate_lower_limit', 'rate_upper_limit')

#     def display_indicative_rate(self, obj):
#         return f"{obj.indicative_rate}%"

#     display_indicative_rate.short_description = 'Indicative Rate'


class InvestmentResource(resources.ModelResource):
    # Define a custom field for the bank name
    bank_name = fields.Field(column_name='bank', attribute='bank',
                             widget=ForeignKeyWidget(BankProduct, 'bank_name'))

    class Meta:
        model = Investment
        fields = ('id', 'bank_name', 'rating_long_term', 'rating_short_term', 'min_investment', 'max_investment',
                  'product_length', 'profit_rate', 'payout_frequency', 'choice_field')
        export_order = ('id', 'bank_name', 'rating_long_term', 'rating_short_term', 'min_investment', 'max_investment',
                        'product_length', 'profit_rate', 'payout_frequency', 'choice_field')

    def before_import_row(self, row, **kwargs):
        # Check if the bank with the specified name exists, create if not
        bank_name = row.get('bank')
        print("======testing=====", bank_name)
        print(row, row.get('profit_rate'))
        if bank_name:
            bank, created = BankProduct.objects.get_or_create(
                bank_name=bank_name)
            row['bank'] = bank  # Set the bank object for the investment
        return super().before_import_row(row, **kwargs)


class InvestmentInline(admin.TabularInline):
    model = Investment
    extra = 1


class BankProductsAdmin(admin.ModelAdmin):
    inlines = [InvestmentInline]


class InvestmentAdmin(ImportExportModelAdmin):

    resource_class = InvestmentResource

    list_display = ['bank', 'min_investment', 'max_investment', 'rating_long_term', 'rating_short_term',
                    'product_length', 'profit_rate', 'payout_frequency', 'choice_field']
    list_filter = ['bank__bank_name', 'choice_field']


admin.site.register(BankProduct, BankProductsAdmin)
admin.site.register(Investment, InvestmentAdmin)
