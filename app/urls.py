from django.urls import path
from . import views



urlpatterns = [

    path("", views.home),
    path("register", views.register),
    path("createTask", views.createTask, name="createTask"),
    path("viewTasks", views.viewTasks, name="viewTasks"),
    path("updateTask/<str:pk>/", views.updateTask, name="updateTask"),
    path("deleteTask/<str:pk>/", views.deleteTask, name="deleteTask"),

]