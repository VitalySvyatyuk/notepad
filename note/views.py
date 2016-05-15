from django.shortcuts import render
from .models import Note

# Create your views here.
def home(request):
    name = "Jefrey"
    text = "Sometext"
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'home.html', context)

def new_note(request):
    name = "Jefrey"
    text = "Sometext"
    context = {
        'name': name,
        'text': text,
    }
    return render(request, 'new_note.html', context)

def note(request, note_id):
    context = {
        'note': Note.objects.get(id=note_id),
    }
    return render(request, 'note.html', context)