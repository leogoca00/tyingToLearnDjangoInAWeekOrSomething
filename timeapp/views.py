from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("<h1>Hello, Django!<\h1>")

def about(request):
    return HttpResponse("About this site")