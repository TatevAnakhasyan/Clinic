# Generated by Django 5.0 on 2023-12-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_generalsliderl_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='generalsliderl',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
