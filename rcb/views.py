from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>King Kohli is Captain</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Patidhar is vicecaptain</h1>')