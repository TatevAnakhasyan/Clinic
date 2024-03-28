# Generated by Django 4.2.7 on 2023-12-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_appus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
                ('text', models.TextField(max_length=255, verbose_name='Text')),
                ('name', models.CharField(max_length=50, verbose_name='Patient Name')),
                ('profession', models.CharField(max_length=50, verbose_name='Profession')),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonies',
                'ordering': ['-id'],
            },
        ),
    ]