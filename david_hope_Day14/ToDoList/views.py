from django.shortcuts import render
from django.http import HttpResponse

tasks = ['eat', 'sleep', 'code', 'repeat']

# Create your views here.
def home(request):
    return render(request, "ToDoList/home.html", {
        'key_tasks': tasks
    })

