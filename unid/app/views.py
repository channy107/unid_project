from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'app/main.html', {})

def index(request):
    return render(request, 'app/index.html', {})

def contentsmain1(request):
    return render(request, 'app/comtentsmain1.html', {})