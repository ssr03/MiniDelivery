# Generated by Django 2.1 on 2019-05-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20190520_1459'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribed_restaurants',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to='restaurant.Restaurant', verbose_name='구독 레스토랑'),
        ),
    ]
