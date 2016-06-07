# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['note_name', 'note_text']


    def clean_note_name(self):
        note_name = self.cleaned_data.get('note_name')
        if note_name == '':
            raise forms.ValidationError("Название не может быть пустым")
        return note_name

    def clean_note_text(self):
        note_text = self.cleaned_data.get('note_text')
        if note_text == '':
            raise forms.ValidationError("Введите текст заметки")
        return note_text
