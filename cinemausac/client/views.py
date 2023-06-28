from django.shortcuts import render, redirect

from datastructures import Movie, FavMovie, NodeCategory, CreditCard
from datastructures import ListaCategoria, ListaPeliculas, ListaFavMovie, ListaTarjetas, ListaTickets, ListaCines

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
        "ListaFavMovie": ListaFavMovie
    })

# * FAVORITE MOVIES
def favMovie(request, categoryOne: str, id: int ):
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    nodeCategory: NodeCategory = ListaCategoria.findNode( categoryOne )
    movie: Movie = nodeCategory.category.movies.findMovie( id )
    favmovie = FavMovie( name, lastName, movie.title, movie.director, movie.year, movie.date, movie.time, movie.image, movie.price )
    ListaFavMovie.append( favmovie )
    return redirect('client:moviesMenu')


# * CARD
def cardMenu(request):
    owner = request.session.get('name')
    creditCard: CreditCard = None
    try:
        if request.method == "POST":
            if( request.POST.get('type') is None and request.POST.get('number') is None and request.POST.get('expiredTime') is None ):
                pass
            else:
                typeC = request.POST.get('type')
                number = request.POST.get('number')
                expiredTime = request.POST.get('expiredTime')
                
                creditCard = CreditCard( typeC, number, owner, expiredTime )
            
    except:
        return render( request, "client/cardMenu.html", {
            "error_message": "Ocurrio un problema, vuelve a registrar"
            })
    else:
        if creditCard is not None:
            ok = ListaTarjetas.push( creditCard )
        
            if ok is not True:
                return render( request, "client/cardMenu.html", {
                    "error_message": "Ocurrio un problema, vuelve a registrar",
                })
            
            return redirect('client:index')
            
    return render(request, 'client/cardMenu.html')

# * SHOP MENU
def shopMenu(request):
    
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    
    obj_Ticket = {}
    
    roomNumber: str = None
    roomSeats: int = None
    
    movieValue: Movie = None
    
    paymentValue: str = None
    
    nit: str = None
    direction: str = None
    
    valid: bool = False
    
    success_message = None
    
    if request.method == "POST":
        valid = True
        theater = request.POST.get('theater')
        number = request.POST.get('room')
        
        for cine in ListaCines:
            if cine.name == theater:
                for room in cine.rooms:
                    if room is not None:
                        if room.number == number:
                            roomNumber = room.number
                            roomSeats = room.seats
                            break
        
        movie = request.POST.get('movie')
        
        for categoria in ListaCategoria:
            for movieOne in categoria.movies:
                if movieOne is not None:
                    if movieOne.title == movie:
                        movieValue = movieOne
                        break
        
        amount = int(request.POST.get('amount'))
        seat: str = request.POST.get('seat')
        
        seatsList = seat.split(',')
        
        if amount != seatsList.__len__():
            return render( request, "client/shopMenu.html", {
            "error_messageSeats": "El número de asientos no seleccionados no coincide con los asientos a comprar"
            })
            
        for seatOne in seatsList:
            if 0 < int(seatOne) <= int(roomSeats):
                pass
            else:
                return render( request, "client/shopMenu.html", {
                    "error_messageSeat": f"El número de asiento { seatOne } seleccionados no cumple con el rango valido"
                })
                
        payment = request.POST.get('payment')
        if payment != "cash":
            paymentValue = "Efectivo"
        else:
            paymentValue = "Tarjeta"
        fact = request.POST.get('fact')
        if fact != "cf":
            nit = request.POST.get('nit')
            direction = request.POST.get('direction')
        else:
            nit = "C/F"
            direction = "C/F"
    
        if ( valid ):
                idF: int = ListaTickets.__len__() + 1

                idFac = f"#USACIPC2_2022110531_{ idF }"

                obj_Ticket = {
                        'id': idFac,
                        'película': movieValue.title,
                        'fecha': movieValue.date,
                        'hora': movieValue.time,
                        'cantidad': amount,
                        'sala': roomNumber,
                        'asientos': seat,
                        'total': amount * int( movieValue.price ),
                        'tipodepago': paymentValue,
                        'nit': nit,
                        'Nombre': name + " " + lastName,
                        'direction': direction,
                        'nameUser': name,
                        'lastNameUser': lastName,
                        'estado': 'Activa'
                    }

                ListaTickets.append(obj_Ticket)
                success_message =  "Tu compra fue registrada correctamente"

    return render(request, 'client/shopMenu.html', {
        "ListaCategoria": ListaCategoria,
        "ListaCines": ListaCines,
        "ListaTarjetas": ListaTarjetas,
        "success_message": success_message,
        "name": name,
        "lastName": lastName
    })
    
def showShops(request):
    name = request.session.get('name')
    lastName = request.session.get('lastName')
    return render(request, 'client/historyMenu.html', {
        "ListaTickets": ListaTickets,
        "name": name,
        "lastName": lastName
    })