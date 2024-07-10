from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hey, there')

def greet_user(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def display (request):
    return render(request, "Starters/home.html")

def randomHTML(request):
    return render(request, "Starters/random.html")

def greet_user_adjusted(request, name):
    return render(request, "Starters/greet.html", {
        "key_name": name.capitalize

    })