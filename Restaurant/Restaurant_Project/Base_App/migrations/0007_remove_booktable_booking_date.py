# Generated by Django 5.1.3 on 2024-11-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0006_alter_booktable_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktable',
            name='Booking_date',
        ),
    ]
