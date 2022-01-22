from django.shortcuts import render
from .models import *
# Create your views here.

def getContextPagesBase():
    context = {}
    context['nbar'] = "home"
    return context

def home(request):
    context = getContextPagesBase()
    return render(request, 'pages/home.html', context)