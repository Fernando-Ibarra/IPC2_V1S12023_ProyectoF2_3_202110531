from django.shortcuts import render, redirect
from datastructures import User, Theater,  MovieRoom, Category,  Movie
from datastructures import NodeUser, NodeTheater, NodeMovieRoom, NodeCategory, NodeMovie
from datastructures import DoubleLinkedListMovieRoom, LinkedListMovie
from datastructures import ListaUsuarios, ListaCines, ListaCategoria, ListaPeliculas

# Create your views here.
def index(request):
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    return render(request, 'myAdmin/index.html', {
        "ListaUsuarios": ListaUsuarios,
        "name": name,
        "lastName": lastName,
    })
    
    
# * USER
    
def userMenu(request):
    user: User = None
    try:
        if request.method == "POST":
            if( request.POST.get('name') is None and request.POST.get('lastName') is None and request.POST.get('email') is None and request.POST.get('password') is None and request.POST.get('phone') is None and request.POST.get('xml') is None):
                pass
            else:
                name = request.POST.get('name')
                lastName = request.POST.get('lastName')
                email = request.POST.get('email')
                password = request.POST.get('password')
                phone = request.POST.get('phone')
                rol = request.POST.get('rol')
                
                user = User( name, lastName, phone, email, password, rol )
            
    except:
        return render( request, "myAdmin/userMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:
        if user is not None:
            nodeuser: NodeUser = NodeUser( user )
            ok = ListaUsuarios.push( nodeuser )
        
            if ok is not True:
                return render( request, "myAdmin/userMenu.html", {
                    "error_message": "Ocurrio un problema, vuelve a registrarte",
                })

            
            return redirect('myAdmin:userMenu')
            
    return render(request, 'myAdmin/userMenu.html', {
        "ListaUsuarios": ListaUsuarios,
    })

def userfromXml(request):
    if request.method == "POST":
        ListaUsuarios.createUserFromXML()
    return redirect('myAdmin:userMenu')

def xmlFromUser(request):
    if request.method == "POST":
        ListaUsuarios.createXMLFromUser()
    return redirect('myAdmin:userMenu')
    
def deleteUser(request, id: int ):
    ListaUsuarios.deleteUser( id )
    return redirect('myAdmin:userMenu')
    
def updateUser(request, id: int):
    if request.method == "POST":
        changes = []
        
        if ( request.POST.get('name') is not "" ):
            name = request.POST.get('name')
            myChanges = {
                "field": "name",
                "value": name
            }
            
            changes.append(myChanges)
        
        if ( request.POST.get('lastName') is not ""):
            lastName = request.POST.get('lastName')
            myChanges = {
                "field": "lastName",
                "value": lastName
            }
            
            changes.append(myChanges)
        
        if ( request.POST.get('email') is not ""):
            email = request.POST.get('email')
            myChanges = {
                "field": "email",
                "value": email
            }
            
            changes.append(myChanges)       
                
        if ( request.POST.get('password') is not ""):
            password = request.POST.get('password')
            myChanges = {
                "field": "password",
                "value": password
            }
            
            changes.append(myChanges)       
        
        if ( request.POST.get('phone') is not ""):
            phone = request.POST.get('phone')
            myChanges = {
                "field": "phoneNumber",
                "value": phone
            }
            
            changes.append(myChanges)
        
        if ( request.POST.get('rol') is not ""):
            rol = request.POST.get('rol')
            myChanges = {
                "field": "rol",
                "value": rol
            }
            
            changes.append(myChanges)     
            
        for change in changes:
            ListaUsuarios.modifyUser( id, change["field"], change["value"] )         
        
        return redirect('myAdmin:userMenu')
    
    return render( request, "myAdmin/userUpdate.html", {
        "id": id
    })


# * THEATER
def theaterMenu(request):
    theater: Theater = None
    try:
        if request.method == "POST":
            if( request.POST.get('name') is None ):
                pass
            else:
                name = request.POST.get('name')
                theater = Theater( name, DoubleLinkedListMovieRoom() )
            
    except:
        return render( request, "myAdmin/theaterMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:
        if theater is not None:
            nodeTheater: NodeTheater = NodeTheater( theater )
            ok = ListaCines.push( nodeTheater )
        
            if ok is not True:
                return render( request, "myAdmin/theaterMenu.html", {
                    "error_message": "Ocurrio un problema, vuelve a registrarte",
                })

            
            return redirect('myAdmin:theaterMenu')
            
    return render(request, 'myAdmin/theaterMenu.html', {
        "ListaCines": ListaCines,
    })
    
def theaterFromXml(request):
    if request.method == "POST":
        ListaCines.createTheatersFromXML()
    return redirect('myAdmin:theaterMenu')

def xmlFromTheater(request):
    if request.method == "POST":
        ListaCines.createXMLFromTheaters()
    return redirect('myAdmin:theaterMenu')

def deleteTheater(request, id: int ):
    ListaCines.deleteTheater( id )
    return redirect('myAdmin:theaterMenu')

def updateTheater(request, id: int):
    if request.method == "POST":
        if ( request.POST.get('name') is not "" ):
            name = request.POST.get('name')
    
        ListaCines.modifyTheater( id, name )        
        
        return redirect('myAdmin:theaterMenu')

    return render( request, "myAdmin/theaterUpdate.html", {
        "id": id
    })
    
# * MOVIE ROOM

def roomMenu(request):
    room: MovieRoom = None
    theaterOne: int = None
    try:
        if request.method == "POST":
            if( request.POST.get('number') is None and request.POST.get('seats') is None and request.POST.get('theater') is None ):
                pass
            else:
                number: str = request.POST.get('number')
                seats: int = int(request.POST.get('seats'))
                room = MovieRoom( number, seats )
                
                theaterOne = int( request.POST.get('theater') )
    except:
        return render( request, "myAdmin/roomMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:
        if room is not None:
            nodeTheater: NodeTheater = ListaCines.findNode( theaterOne )
            if nodeTheater is not None:
                ok = nodeTheater.theater.rooms.push( room )

                if ok is not True:
                    return render( request, "myAdmin/roomMenu.html", {
                        "error_message": "Ocurrio un problema, vuelve a registrarte",
                    })
                
                return redirect('myAdmin:roomMenu')

            return render( request, "myAdmin/roomMenu.html", {
                        "ListaCines": ListaCines,
                        "error_message": "Ocurrio un problema, vuelve a registrarte",
                    })
            
    return render(request, 'myAdmin/roomMenu.html', {
        "ListaCines": ListaCines,
    })
    
def deleteRoom(request, theaterOne: str, id: int ):
    nodeTheater: NodeTheater = ListaCines.findNodeByName( theaterOne )
    if nodeTheater is not None:
        nodeRoom: NodeMovieRoom = nodeTheater.theater.rooms.findNode( id )
        if nodeRoom is not None:
            nodeTheater.theater.rooms.deleteNode( nodeRoom )
    return redirect('myAdmin:roomMenu')

def updateRoom(request, theaterOne: str, id: int ):
    nodeTheater: NodeTheater = ListaCines.findNodeByName( theaterOne )
    if nodeTheater is not None:
        if request.method == "POST":
            changes = []
            
            if ( request.POST.get('number') is not "" ):
                number = request.POST.get('number')
                myChanges = {
                    "field": "number",
                    "value": number
                }
                changes.append(myChanges)
            
            if ( request.POST.get('seats') is not "" ):
                seats = request.POST.get('seats')
                myChanges = {
                    "field": "seats",
                    "value": seats
                }
                changes.append(myChanges)
            
            for change in changes:
                nodeTheater.theater.rooms.modifyMovieRoom( id, change["field"], change["value"] )

            return redirect('myAdmin:roomMenu')

    return render( request, "myAdmin/roomUpdate.html", {
        "id": id,
        "theaterOne": theaterOne
    })
    
# * CATEGORY

def categoryMenu(request):
    category: Category = None
    try:
        if request.method == "POST":
            if( request.POST.get('name') is None ):
                pass
            else:
                name = request.POST.get('name')
                category = Category( name, LinkedListMovie() )
    except:
        return render( request, "myAdmin/categoryMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:
        if category is not None:
            ok = ListaCategoria.push( category )
        
            if ok is not True:
                return render( request, "myAdmin/categoryMenu.html", {
                    "error_message": "Ocurrio un problema, vuelve a registrarte",
                })

            
            return redirect('myAdmin:categoryMenu')
            
    return render(request, 'myAdmin/categoryMenu.html', {
        "ListaCategoria": ListaCategoria,
    })
    
def categoryFromXml(request):
    if request.method == "POST":
        ListaCategoria.createCategoriesFromXML()
    return redirect('myAdmin:categoryMenu')

def xmlFromCategory(request):
    if request.method == "POST":
        ListaCategoria.createXMLFromCategories()
    return redirect('myAdmin:categoryMenu')

def deleteCategory(request, id: int ):
    ListaCategoria.delete( id )
    return redirect('myAdmin:categoryMenu')

def updateCategory(request, id: int):
    if request.method == "POST":
        if ( request.POST.get('name') is not "" ):
            name = request.POST.get('name')
    
        ListaCategoria.modify( id, name )        
        
        return redirect('myAdmin:categoryMenu')

    return render( request, "myAdmin/categoryUpdate.html", {
        "id": id
    })

# * MOVIE

def movieMenu(request):
    movie: Movie = None
    categoryOne: int = None
    try:
        if request.method == "POST":
            if( request.POST.get('title') is None and request.POST.get('director') is None and request.POST.get('category') is None and request.POST.get('year') is None and request.POST.get('date') is None and request.POST.get('time') is None and request.POST.get('image') is None and request.POST.get('price') is None ):
                pass
            else:
                title: str = request.POST.get('title')
                director: str = request.POST.get('director')
                year: str = request.POST.get('year')
                date: str = request.POST.get('date')
                time: str = request.POST.get('time')
                image: str = request.POST.get('image')
                price: int = int(request.POST.get('price'))
                movie = Movie( title, director, year, date, time, image, price )
                
                categoryOne = int( request.POST.get('category') )
    except:
        return render( request, "myAdmin/movieMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:
        if movie is not None:
            nodeMovie: NodeMovie = NodeMovie( movie ) 
            nodeCategory: NodeCategory = ListaCategoria.findNode( categoryOne )
            if nodeCategory is not None:
                ok = nodeCategory.category.movies.push( nodeMovie )

                if ok is not True:
                    return render( request, "myAdmin/movieMenu.html", {
                        "error_message": "Ocurrio un problema, vuelve a registrarte",
                    })
                
                return redirect('myAdmin:movieMenu')

            return render( request, "myAdmin/movieMenu.html", {
                        "ListaCategoria": ListaCategoria,
                        "error_message": "Ocurrio un problema, vuelve a registrarte",
                    })
            
    return render(request, 'myAdmin/movieMenu.html', {
        "ListaCategoria": ListaCategoria,
    })

def removeMovie(request, categoryOne: str, id: int ):
    nodeCategory: NodeCategory = ListaCategoria.findNode( categoryOne )
    if nodeCategory is not None:
        nodeCategory.category.movies.deleteMovie( id )
    return redirect('myAdmin:movieMenu')

def updateMovie(request, categoryOne: str, id: int ):
    nodeCategory: NodeCategory = ListaCategoria.findNode( categoryOne )
    if nodeCategory is not None:
        if request.method == "POST":
            changes = []
            
            if ( request.POST.get('title') is not "" ):
                title: str = request.POST.get('title')
                myChanges = {
                    "field": "title",
                    "value": title
                }
                changes.append(myChanges)
            
            if ( request.POST.get('director') is not "" ):
                director = request.POST.get('director')
                myChanges = {
                    "field": "director",
                    "value": director
                }
                changes.append(myChanges)
            
            if ( request.POST.get('year') is not "" ):
                year = request.POST.get('year')
                myChanges = {
                    "field": "year",
                    "value": year
                }
                changes.append(myChanges)
            
            if ( request.POST.get('date') is not "" ):
                date = request.POST.get('date')
                myChanges = {
                    "field": "date",
                    "value": date
                }
                changes.append(myChanges)
            
            if ( request.POST.get('time') is not "" ):
                time = request.POST.get('time')
                myChanges = {
                    "field": "time",
                    "value": time
                }
                changes.append(myChanges)
            
            if ( request.POST.get('image') is not "" ):
                image = request.POST.get('image')
                myChanges = {
                    "field": "image",
                    "value": image
                }
                changes.append(myChanges)
            
            if ( request.POST.get('price') is not "" ):
                price = request.POST.get('price')
                myChanges = {
                    "field": "price",
                    "value": price
                }
                changes.append(myChanges)
                
            for change in changes:
                nodeCategory.category.movies.modifyMovie( id, change["field"], change["value"] )

            return redirect('myAdmin:movieMenu')

    return render( request, "myAdmin/movieUpdate.html", {
        "id": id,
        "categoryOne": categoryOne
    })