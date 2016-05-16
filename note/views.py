from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
import datetime

# Create your views here.
def home(request):
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'home.html', context)

def new(request):
    if request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {
                'form': form
            }
            print form, type(form)
            return render(request, 'new_note.html', context)
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