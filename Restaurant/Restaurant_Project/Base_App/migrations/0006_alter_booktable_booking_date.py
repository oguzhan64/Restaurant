# Generated by Django 5.1.3 on 2024-11-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0005_booktable_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='Booking_date',
            field=models.CharField(max_length=55),
        ),
    ]