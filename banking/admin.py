import csv
import json

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from .models import (Article, BankProduct, ConventionalFund, InsuranceProduct,
                     Investment, IslamicFund, LifeInsuranceCompany)

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

    investment_type = fields.Field(
        column_name='investment_type', attribute='investment_type')

    class Meta:
        model = Investment
        fields = ('id', 'bank_name', 'rating_long_term', 'rating_short_term', 'min_investment', 'max_investment',
                  'product_length', 'profit_rate', 'payout_frequency', 'choice_field', 'investment_type')
        export_order = ('id', 'bank_name', 'rating_long_term', 'rating_short_term', 'min_investment', 'max_investment',
                        'product_length', 'profit_rate', 'payout_frequency', 'choice_field', 'investment_type')

    def before_import_row(self, row, **kwargs):
        # Check if the bank with the specified name exists, create if not
        bank_name = row.get('bank')
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
                    'product_length', 'profit_rate', 'payout_frequency', 'choice_field', 'investment_type']
    list_filter = ['bank__bank_name', 'choice_field', 'investment_type']


class InsuranceProductResource(resources.ModelResource):
    # Define a custom field for the company name
    company_name = fields.Field(column_name='company', attribute='company',
                                widget=ForeignKeyWidget(LifeInsuranceCompany, 'company_name'))

    class Meta:
        model = InsuranceProduct
        fields = ('id', 'company_name', 'rating', 'min_eligibility_age', 'max_eligibility_age', 'max_maturity_age',
                  'minimum_premium', 'product_length', 'min_policy_term', 'max_policy_term', 'contribution_allocation',
                  'premium_frequency', 'loan_against_premium_paid', 'free_look_up_period', 'partial_full_withdrawal',
                  'inflation_protection', 'charges', 'bonus_allocation', 'product_benefit_1', 'product_benefit_2',
                  'product_benefit_3', 'product_benefit_4', 'product_benefit_5', 'product_benefit_6', 'product_benefit_7',
                  'optional_benefits')
        export_order = ('id', 'company_name', 'rating', 'min_eligibility_age', 'max_eligibility_age', 'max_maturity_age',
                        'minimum_premium', 'product_length', 'min_policy_term', 'max_policy_term', 'contribution_allocation',
                        'premium_frequency', 'loan_against_premium_paid', 'free_look_up_period', 'partial_full_withdrawal',
                        'inflation_protection', 'charges', 'bonus_allocation', 'product_benefit_1', 'product_benefit_2',
                        'product_benefit_3', 'product_benefit_4', 'product_benefit_5', 'product_benefit_6', 'product_benefit_7',
                        'optional_benefits')

    def before_import_row(self, row, **kwargs):
        # Check if the bank with the specified name exists, create if not
        company_name = row.get('company')
        print("======testing=====", company_name)
        if company_name:
            company, created = LifeInsuranceCompany.objects.get_or_create(
                company_name=company_name)
            row['company'] = company  # Set the bank object for the investment
        return super().before_import_row(row, **kwargs)


class InsuranceProductInline(admin.TabularInline):
    model = InsuranceProduct
    extra = 1


class LifeInsuranceAdmin(admin.ModelAdmin):
    inlines = [InsuranceProductInline]


class InsuranceProductAdmin(ImportExportModelAdmin):

    resource_class = InsuranceProductResource

    list_display = ['company', 'rating',
                    'product_length', 'premium_frequency']
    list_filter = ['company__company_name', 'premium_frequency']


class IslamicFundResource(resources.ModelResource):
    class Meta:
        model = IslamicFund
        # Exclude the JSON field if you don't want it in the export
        # exclude = ('ytd_as_of_date',)


class IslamicFundAdmin(ImportExportModelAdmin):
    resource_class = IslamicFundResource
    list_display = [
        'fund_name',
        'fund_type',
        'objective',
        'fund_size',
        'minimum_investment_in_pkr',
        'front_end_load',
        'management_fee',
        'risk',
        'tenor_period',
        'back_end_load',
        'benchmark',
        'pricing',
        'launch_date',
        'category',
        'features',
        'no_lock_in_period',
        'retain_for_24_months',
        'easy_redemption',
        'max_preservation_of_capital',
        'systematic_investment_plan_facility',
        'tax_benefits',
        'rating',
        'performance',
        'return_field'
    ]

    # def get_ytd_2020(self, obj):
    #     return json.loads(obj.ytd_as_of_date).get('2020', '-')
    # get_ytd_2020.short_description = 'YTD 2020'

    # def get_ytd_2021(self, obj):
    #     return json.loads(obj.ytd_as_of_date).get('2021', '-')
    # get_ytd_2021.short_description = 'YTD 2021'

    # def get_ytd_2022(self, obj):
    #     return json.loads(obj.ytd_as_of_date).get('2022', '-')
    # get_ytd_2022.short_description = 'YTD 2022'


# Register your model with the custom admin class


class ConventionalFundResource(resources.ModelResource):
    class Meta:
        model = ConventionalFund


class ConventionalFundAdmin(ImportExportModelAdmin):
    resource_class = ConventionalFundResource
    list_display = [
        'fund_name',
        'fund_type',
        'objective',
        'fund_size',
        'minimum_investment_in_pkr',
        'front_end_load',
        'management_fee',
        'risk',
        'tenor_period',
        'back_end_load',
        'benchmark',
        'pricing',
        'launch_date',
        'category',
        'features',
        'no_lock_in_period',
        'retain_for_24_months',
        'easy_redemption',
        'max_preservation_of_capital',
        'systematic_investment_plan_facility',
        'tax_benefits',
        'rating',
        'performance',
        'return_field'
    ]


admin.site.register(IslamicFund, IslamicFundAdmin)
admin.site.register(ConventionalFund, ConventionalFundAdmin)
admin.site.register(BankProduct, BankProductsAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(LifeInsuranceCompany, LifeInsuranceAdmin)
admin.site.register(InsuranceProduct, InsuranceProductAdmin)
admin.site.register(Article)
