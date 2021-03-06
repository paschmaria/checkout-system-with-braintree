# Generated by Django 3.0.5 on 2020-04-15 20:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('orders', '0003_auto_20200415_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupons.Coupon', verbose_name='coupon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='paid'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='postal code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
