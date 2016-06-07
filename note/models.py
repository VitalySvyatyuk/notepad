from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.

class Note(models.Model):
    class Meta:
        db_table = 'note'

    note_name = models.CharField(max_length=200, blank=True)
    note_text = models.CharField(max_length=2000, blank=True)
    note_date = models.DateTimeField(default=datetime.datetime.now())

