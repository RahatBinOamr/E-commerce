# Generated by Django 4.2.6 on 2023-11-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='product_image_model',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
