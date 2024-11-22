# Generated by Django 5.1.3 on 2024-11-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0003_alter_items_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='Image',
        ),
        migrations.AddField(
            model_name='items',
            name='Item_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='Price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='media/items'),
        ),
    ]