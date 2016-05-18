from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Note
import forms
import datetime

# Create your views here.
def home(request):
    context = {
        'notes': Note.objects.all().order_by('-id')
    }
    return render(request, 'home.html', context)

def new(request):
    if request.POST:
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            send_mail(
                'Note from {}'.format(form.cleaned_data['note_name']),
                form.cleaned_data['note_text'],
                'genrich <genrich_sabakevich@mail.ru>',
                #EXAMPLE: '{name} <{email}>'.format(**form.cleaned_data),
                ['goodgame1945@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Email is sent.')

            form.save()
            return redirect('/')
        else:
            context = {
                'form': form
            }
            print form, type(form)
            return render(request, 'new_note.html', context)
    form = forms.NoteForm
    context = {
        'form': form
    }
    return render(request, 'new_note.html', context)

def note(request, note_id):
    context = {
        'note': Note.objects.get(id=note_id),
    }
    return render(request, 'note.html', context)