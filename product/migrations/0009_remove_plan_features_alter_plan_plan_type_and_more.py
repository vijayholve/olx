# Generated by Django 5.1.2 on 2024-11-05 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_plan_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='features',
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('one time', 'One Time'), ('recurring', 'Recurring')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='PlanFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('included', models.BooleanField(default=False)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.features')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.plan')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='features',
            field=models.ManyToManyField(through='product.PlanFeature', to='product.features'),
        ),
    ]