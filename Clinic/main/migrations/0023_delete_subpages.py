# Generated by Django 4.2.7 on 2023-12-14 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_pages_subpages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubPages',
        ),
    ]