# Generated by Django 5.1.2 on 2024-11-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]