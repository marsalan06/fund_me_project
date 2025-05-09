# Generated by Django 4.2.1 on 2024-12-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0024_investment_currency_alter_investment_choice_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'US Dollar'), ('GBP', 'British Pound'), ('EUR', 'Euro'), ('AED', 'UAE Dirham'), ('SAR', 'Saudi Riyal')], max_length=3, null=True),
        ),
    ]
