from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datastructures import User, ListaUsuarios, NodeUser

# Create your views here.
def index(request):
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    return render(request, 'myAdmin/index.html', {
        "ListaUsuarios": ListaUsuarios,
        "name": name,
        "lastName": lastName,
    })
    
def users(request):
    return render(request, 'myAdmin/index.html', {
        "ListaUsuarios": ListaUsuarios,
    })