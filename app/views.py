from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm



def home(request):

    #Nesse exemplo pegamos todos os dados, no ativo escolhemos qual usar.
    #queryAllData = Task.objects.all()
    #context = {"tasks": queryAllData}

    querySingleData = Task.objects.get(id=4)
    context = {"task": querySingleData}

    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def createTask(request):
    form = TaskForm()
    context = {"form": form}
    return render(request, "taskForm.html", context=context)




