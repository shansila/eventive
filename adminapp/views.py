from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'homead.html')
# Create your views here.
def about(request):
    return render(request, 'aboutad.html')

def profile(request):
    return render(request, 'profilead.html')


def birthday(request):
    return render(request, 'birthdayexperiances.html')


def wedding(request):
    return render(request, 'weddingexperiances.html')