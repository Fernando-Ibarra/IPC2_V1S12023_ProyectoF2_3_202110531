from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "client"

urlpatterns = [
    # * index
    path('', views.index, name="index"),
    
    # * MOVIES 
    path('movies/', views.movieMenu, name="moviesMenu"),
]