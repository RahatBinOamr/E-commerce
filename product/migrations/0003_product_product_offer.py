# Generated by Django 4.2.6 on 2023-11-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_product_price_product_product_current_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(default=0),
        ),
    ]
