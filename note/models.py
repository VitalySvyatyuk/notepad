from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Note(models.Model):
    class Meta:
        db_table = 'note'

    note_date = models.DateTimeField()
    note_name = models.CharField(max_length=200)
    note_text = models.CharField(max_length=2000, blank=True)
