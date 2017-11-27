# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 05:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True,null =True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.TextField(blank=True),
        ),
    ]