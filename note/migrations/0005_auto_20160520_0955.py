# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 06:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20160516_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 20, 9, 55, 57, 181000)),
        ),
    ]
