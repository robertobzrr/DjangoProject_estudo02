from django.urls import path
from . import views



urlpatterns = [

    path("", views.home),
    path("register", views.register),
    path("createTask", views.createTask),

]