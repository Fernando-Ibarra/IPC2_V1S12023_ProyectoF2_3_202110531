from django.shortcuts import render, redirect
from datastructures import User, NodeUser, Theater, NodeTheater, MovieRoom, NodeMovieRoom, DoubleLinkedListMovieRoom
from datastructures import ListaUsuarios, ListaCines

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