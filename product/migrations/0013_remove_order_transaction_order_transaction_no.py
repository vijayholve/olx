# Generated by Django 5.1.2 on 2024-11-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_order_transaction_no_order_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_no',
            field=models.CharField(blank=True, max_length=36, unique=True),
        ),
    ]
