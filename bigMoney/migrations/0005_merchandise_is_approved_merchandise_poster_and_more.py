# Generated by Django 4.1.7 on 2023-04-04 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigMoney', '0004_user_orders_user_shoppingcart_user_available_merch'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='is_approved',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=None, null=True),
        ),
    ]