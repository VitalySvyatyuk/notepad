# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_auto_20160520_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 10, 23, 7, 125000)),
        ),
    ]
