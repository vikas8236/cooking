# Generated by Django 5.0.6 on 2024-06-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0003_rename_category_restaurants_menue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='offer',
            field=models.CharField(default='50% aboove 199', max_length=500),
        ),
    ]
