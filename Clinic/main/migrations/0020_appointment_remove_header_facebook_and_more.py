# Generated by Django 5.0 on 2023-12-13 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_feature_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='header',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='header',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='header',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='header',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='header',
            name='youtube',
        ),
        migrations.RemoveField(
            model_name='ourdoctors',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='ourdoctors',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='ourdoctors',
            name='twitter',
        ),
        migrations.AddField(
            model_name='aboutstore',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='aboutstore',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram URL'),
        ),
        migrations.AddField(
            model_name='aboutstore',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='Linkedin URL'),
        ),
        migrations.AddField(
            model_name='aboutstore',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitter URL'),
        ),
        migrations.AddField(
            model_name='aboutstore',
            name='youtube',
            field=models.URLField(blank=True, verbose_name='Youtube'),
        ),
        migrations.AddField(
            model_name='ourdoctors',
            name='aboutstore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aboutdoc', to='main.aboutstore'),
        ),
        migrations.AlterField(
            model_name='header',
            name='aboutstore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aboutheder', to='main.aboutstore'),
        ),
    ]
