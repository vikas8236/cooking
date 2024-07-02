# Generated by Django 5.0.6 on 2024-07-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='imageURL',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
