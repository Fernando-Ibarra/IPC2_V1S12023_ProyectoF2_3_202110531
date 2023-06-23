from django.shortcuts import render, redirect

from datastructures import ListaCategoria, ListaPeliculas

# Create your views here.
def index(request):
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    return render(request, 'client/index.html', {
        "name": name,
        "lastName": lastName,
    })
    
# * MOVIES

def movieMenu(request):
    return render(request, 'client/moviesMenu.html', {
        "ListaCategoria": ListaCategoria,
        "ListaPeliculas": ListaPeliculas,
    })