# Generated by Django 4.2.1 on 2023-11-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0005_alter_investment_profit_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='max_investment',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='investment',
            name='min_investment',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]