# Generated by Django 4.0.1 on 2022-01-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0004_rename_earliest_arrive_date_ride_arrive_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrive_date',
            field=models.DateTimeField(help_text='Format: 2022-01-01 12:00'),
        ),
    ]
