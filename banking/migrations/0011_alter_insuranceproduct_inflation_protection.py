# Generated by Django 4.2.1 on 2023-12-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0010_alter_insuranceproduct_contribution_allocation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceproduct',
            name='inflation_protection',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
