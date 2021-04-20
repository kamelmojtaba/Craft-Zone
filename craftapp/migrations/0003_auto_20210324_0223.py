# Generated by Django 3.1.6 on 2021-03-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craftapp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]