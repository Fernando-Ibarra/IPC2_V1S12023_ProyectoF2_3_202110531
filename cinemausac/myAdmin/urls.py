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
    path('category/', views.index, name="categoryMeny"),
    # TODO: UPDATE -> path('category/update/<int:id>', views., name="categoryUpdate")
    # TODO: DELETE -> path('category/delete/<int:id>', views., name="categoryDelete")
    # TODO: IMPORT XML -> path('category/xml/', views., name="categoryXml")
    # TODO: EXPORT XML -> path('category/xml/export', views., name="xmlCategory")
    
    # * movie
    path('movie/', views.index, name="movieMenu"),
    # TODO: UPDATE -> path('movie/update/<str:category>/<int:id>', views., name="movieUpdate")
    # TODO: DELETE -> path('movie/delete/<str:category>/<int:id>', views., name="movieDelete")
    
    # * theater
    path('theater/', views.theaterMenu, name="theaterMenu"),
    path('theater/update/<int:id>', views.updateTheater, name="theaterUpdate"),
    path('theater/delete/<int:id>', views.deleteTheater, name="theaterDelete"),
    path('theater/xml/', views.theaterFromXml, name="theaterXml"),
    path('theater/xml/export', views.xmlFromTheater, name="xmlTheater"),
    
    # * room
    path('room/', views.index, name="roomMenu"),
    # TODO: UPDATE -> path('room/update/<str:theater>/<int:id>', views., name="roomUpdate")
    # TODO: DELETE -> path('room/delete/<str:theater>/<int:id>', views., name="roomDelete")
    # TODO: IMPORT XML -> path()
    # TODO: EXPORT XML -> path()
    
    # * ticket
    path('ticket/', views.index, name="ticketMenu"),
    # TODO: UPDATE -> path('ticket/update/<int:id>', views., name="ticketUpdate")
    # TODO: DELETE -> path('ticket/delete/<int:id>', views., name="ticketDelete")
    
    # * CREDIT CARD
    
    # * MOVIE LIST
    
]