from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'name': name,
        'text': text,
    }
    return render(request, 'home.html', context)
