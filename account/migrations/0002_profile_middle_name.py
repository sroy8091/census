# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-27 20:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(default=datetime.datetime(2017, 5, 27, 20, 40, 59, 145915, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
