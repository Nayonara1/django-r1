from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP RESPONDE 


def home(request):
 return HttpResponse('Home.html')

def  sobre(request):
 return HttpResponse('<h1>Sobre-  Django</h1>')

def contato(request):   
 return HttpResponse('<h1>Contato- Django</h1>')
