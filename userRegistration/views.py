from django.shortcuts import render, redirect
from django.http import HttpResponse # allow us to send a response to the user

# Create your views here.

def home(request):
    """Render home page"""
    return render(request, 'home.html')