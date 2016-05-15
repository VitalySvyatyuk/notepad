from django.shortcuts import render
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    name = "Jefrey"
    text = "Sometext"
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'home.html', context)

def new(request):
    form = NoteForm
    context = {
        'form': form
    }
    return render(request, 'new_note.html', context)

def note(request, note_id):
    context = {
        'note': Note.objects.get(id=note_id),
    }
    return render(request, 'note.html', context)