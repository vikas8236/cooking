# Generated by Django 5.0.6 on 2024-07-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_student_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OTP',
        ),
    ]
