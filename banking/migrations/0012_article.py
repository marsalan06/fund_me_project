# Generated by Django 4.2.1 on 2023-12-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0011_alter_insuranceproduct_inflation_protection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='previews/')),
            ],
        ),
    ]
