# Generated by Django 4.0.1 on 2022-01-31 03:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='vehicle_capacity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
