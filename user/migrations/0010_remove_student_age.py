# Generated by Django 5.0.6 on 2024-07-02 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_delete_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
