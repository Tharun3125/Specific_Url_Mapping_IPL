from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>Ruturaj is Captain</h2>')

def vicecaptain(request):
    return HttpResponse('<h1>Jadeja is Vice Captain</h1>')