# Generated by Django 4.2.7 on 2023-12-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Image'),
        ),
    ]
