# Generated by Django 4.2.1 on 2025-01-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0031_investment_is_expected_profit_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='profit_rate',
            field=models.CharField(max_length=100),
        ),
    ]
