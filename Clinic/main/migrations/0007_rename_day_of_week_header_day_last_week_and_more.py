# Generated by Django 5.0 on 2023-12-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_header_day_of_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='day_of_week',
            new_name='day_last_week',
        ),
        migrations.AddField(
            model_name='header',
            name='day_one_week',
            field=models.IntegerField(null=True),
        ),
    ]
