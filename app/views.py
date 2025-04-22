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




def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("viewTasks")

    context = {"form":form}
    return render(request, "updateTask.html", context=context)




def deleteTask(request, pk):

    task = Task.objects.get(id=pk)
    
    if request.method == "POST":
        task.delete()

        return redirect("viewTasks")
    

    context = {"object":task}
    return render(request, "deleteTask.html", context=context)
