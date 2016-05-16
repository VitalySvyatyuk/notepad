from django.contrib import admin
from .models import Note
from .forms import NoteForm



admin.site.register(Note)
