from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'no1/index.html', {'title': 'home'})

