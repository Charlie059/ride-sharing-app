# Generated by Django 4.0.1 on 2022-01-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0013_alter_ride_passenger_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='seat_available',
            field=models.IntegerField(default=0),
        ),
    ]
