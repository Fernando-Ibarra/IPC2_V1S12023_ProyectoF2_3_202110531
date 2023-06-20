from django.urls import path
from . import views

app_name = "myAdmin"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.index, name="index"),
    path('categories/', views.index, name="index"),
    path('movies/', views.index, name="index"),
    path('theaters/', views.index, name="index"),
    path('rooms/', views.index, name="index"),
    path('tickets/', views.index, name="index"),
]