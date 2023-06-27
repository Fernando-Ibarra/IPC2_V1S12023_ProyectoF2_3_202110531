from django.contrib import admin
from django.urls import path
from . import views

app_name = "client"

urlpatterns = [
    # * index
    path('', views.index, name="index"),
    
    # * MOVIES 
    path('movies/', views.movieMenu, name="moviesMenu"),
    
    # * FAVORITE MOVIES
    path('movies/fav/<str:categoryOne>/<int:id>/', views.favMovie, name="favoriteMovie"),
    
    # * CARD 
    path('card/create/', views.cardMenu, name="cardMenu"),
    
    # * Shops
    path('buy/', views.shopMenu, name="shopMenu"),
    
    # * History Shops
    path('history/buys', views.showShops, name="historyMenu"),
]