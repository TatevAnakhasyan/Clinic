# Generated by Django 4.2.7 on 2023-12-14 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_ourdoctors_aboutstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='SubPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='SubPage Name')),
                ('pages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subpage', to='main.pages')),
            ],
            options={
                'verbose_name': 'Sub Page',
                'verbose_name_plural': 'Sub Pages',
            },
        ),
    ]
