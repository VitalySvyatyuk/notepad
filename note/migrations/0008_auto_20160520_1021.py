# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20160520_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 10, 21, 55, 665000)),
        ),
    ]
