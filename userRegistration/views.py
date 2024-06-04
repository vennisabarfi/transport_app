from django.shortcuts import render
from django import HttpResponse

# Create your views here.
def detail(request, question_id):
    return HttpResponse("Youre looking st this")