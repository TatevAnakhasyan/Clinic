# Generated by Django 5.0 on 2023-12-11 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_day_of_week_header_day_last_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='day_last_week',
        ),
        migrations.RemoveField(
            model_name='header',
            name='day_one_week',
        ),
    ]
