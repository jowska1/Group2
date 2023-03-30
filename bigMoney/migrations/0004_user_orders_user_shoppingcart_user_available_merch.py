# Generated by Django 4.1.7 on 2023-03-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigMoney', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Orders',
            field=models.ManyToManyField(default=None, to='bigMoney.order'),
        ),
        migrations.AddField(
            model_name='user',
            name='ShoppingCart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bigMoney.shoppingcart'),
        ),
        migrations.AddField(
            model_name='user',
            name='available_merch',
            field=models.ManyToManyField(default=None, to='bigMoney.merchandise'),
        ),
    ]
