# Generated by Django 5.0 on 2023-12-14 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_slidapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slidapp',
            name='title',
        ),
    ]