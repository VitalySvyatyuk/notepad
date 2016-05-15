from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Jefrey"
    text = "Sometext"
    context = {
        'name': name,
        'text': text,
    }
    return render(request, 'home.html', context)

def note(request):
    name = "Jefrey"
    text = "Sometext"
    context = {
        'name': name,
        'text': text,
    }
    return render(request, 'note.html', context)