# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasuntu', '0015_auto_20180321_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistpage',
            name='picture',
            field=models.CharField(default='https://ryanboudnotisahackdotcom.files.wordpress.com/2017/02/266c2fa0-9909-4e54-bb45-a4ef515e404f.jpg', max_length=400),
        ),
    ]