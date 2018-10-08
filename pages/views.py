from django.shortcuts import render
from pages.namer import namer

# Create your views here.

def home(request):
    return render(request, 'home.html', {'out_text': namer})

def about(request):
    my_name = 'Hello, my name is Ian Brooks'
    return render(request, 'about.html', {'my_name': my_name})

def contact(request):
    return render(request, 'contact.html', {})
