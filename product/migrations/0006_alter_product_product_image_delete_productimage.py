# Generated by Django 4.2.6 on 2023-11-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='productImages/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]