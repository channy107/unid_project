from django.shortcuts import render
from django.http import HttpResponse

# Controler

def two(request):
    return HttpResponse('<h1>Second!!!</h1>')
