from django.urls import path
from . import views

app_name = "myAdmin"

urlpatterns = [
    # * index
    path('', views.index, name="index"),
    
    # * user
    path('user/', views.userMenu, name="userMenu"),
    path('user/update/<int:id>', views.updateUser, name="userUpdate"),
    path('user/delete/<int:id>',  views.deleteUser, name="userDelete"),
    path('user/xml/', views.userfromXml, name="userXml"),
    path('user/xml/export', views.xmlFromUser, name="xmlUser"),
    
    # * category
    path('category/', views.categoryMenu, name="categoryMenu"),
    path('category/update/<int:id>', views.updateCategory, name="categoryUpdate"),
    path('category/delete/<int:id>', views.deleteCategory, name="categoryDelete"),
    path('category/xml/', views.categoryFromXml, name="categoryXml"),
    path('category/xml/export', views.xmlFromCategory, name="xmlCategory"),
    
    # * movie
    path('movie/', views.movieMenu, name="movieMenu"),
    # TODO: UPDATE -> path('movie/update/<str:categoryOne>/<int:id>', views., name="movieUpdate")
    path('movie/delete/<str:categoryOne>/<int:id>', views.removeMovie, name="movieDelete"),
    
    # * theater
    path('theater/', views.theaterMenu, name="theaterMenu"),
    path('theater/update/<int:id>', views.updateTheater, name="theaterUpdate"),
    path('theater/delete/<int:id>', views.deleteTheater, name="theaterDelete"),
    path('theater/xml/', views.theaterFromXml, name="theaterXml"),
    path('theater/xml/export', views.xmlFromTheater, name="xmlTheater"),
    
    # * room
    path('room/', views.roomMenu, name="roomMenu"),
    path('room/update/<str:theaterOne>/<int:id>', views.updateRoom, name="roomUpdate"),
    path('room/delete/<str:theaterOne>/<int:id>', views.deleteRoom, name="roomDelete"),

    
    # * ticket
    path('ticket/', views.index, name="ticketMenu"),
    # TODO: UPDATE -> path('ticket/update/<int:id>', views., name="ticketUpdate")
    
    # * CREDIT CARD
    
    # * MOVIE LIST
    
]