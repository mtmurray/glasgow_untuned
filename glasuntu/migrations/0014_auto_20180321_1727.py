# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glasuntu', '0013_auto_20180321_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='glasuntu.ArtistPage'),
        ),
    ]
