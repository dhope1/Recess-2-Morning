from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hey, there')

def greet_user(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def display (request):
    return render(request, "Starters/home.html")