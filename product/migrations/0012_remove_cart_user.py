# Generated by Django 4.2.6 on 2023-11-30 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
