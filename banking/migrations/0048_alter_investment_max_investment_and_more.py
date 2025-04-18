# Generated by Django 4.2.1 on 2025-02-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0047_alter_insuranceproduct_max_eligibility_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='max_investment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='min_investment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='rating_long_term',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='rating_short_term',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
