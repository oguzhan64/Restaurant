# Generated by Django 5.1.3 on 2024-11-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_remove_items_item_name_remove_items_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='items/'),
        ),
    ]
