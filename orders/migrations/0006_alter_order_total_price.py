# Generated by Django 5.0.1 on 2024-02-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_mobile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]