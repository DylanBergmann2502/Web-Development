# Generated by Django 4.1.5 on 2023-02-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pbulic',
            field=models.BooleanField(default=True),
        ),
    ]
