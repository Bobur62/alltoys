# Generated by Django 3.1.5 on 2021-01-13 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0005_auto_20210113_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
