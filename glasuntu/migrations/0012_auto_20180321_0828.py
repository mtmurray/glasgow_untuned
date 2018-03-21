# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasuntu', '0011_auto_20180320_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuepage',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='venuepage',
            name='genre',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='venuepage',
            name='picture',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKh6zi1IdUc7vNzKuyCT_AgHj8GxpBUBjZ-0rCtk5GmSOJoMKjRQ', max_length=400),
        ),
    ]
