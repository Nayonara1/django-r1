from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Nayonara Galvão'})

def sobre(request):
    return HttpResponse('<h1>Sobre - Hello Django</h1>')

def contato(request):
    return HttpResponse('<h1>Contato - Hello Django</h1>')