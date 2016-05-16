from django.contrib import admin
from .models import Note
from .forms import NoteForm

class AddForm(admin.ModelAdmin):
    form = NoteForm

admin.site.register(Note, AddForm)
