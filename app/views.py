from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm



def home(request):
    return render(request, "index.html")



def register(request):
    return render(request, "register.html")



def createTask(request):
    form = TaskForm()

    if request.method == "POST":

        form = TaskForm(request.POST)


        if form.is_valid():

            form.save()

            return redirect("viewTasks")

    context = {"form":form}

    return render(request, "createTask.html", context=context)




def viewTasks(request):

    tasks = Task.objects.all()

    context = {"tasks":tasks}

    return render(request, "viewTasks.html", context=context)




