# Generated by Django 5.0.1 on 2024-01-29 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0002_product_cat_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat_name',
        ),
    ]