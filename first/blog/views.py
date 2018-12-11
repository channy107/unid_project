from django.shortcuts import render
from django.http import HttpResponse

def one(request):
    return HttpResponse('Hello')
