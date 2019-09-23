# Generated by Django 2.1 on 2019-05-20 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grid',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
