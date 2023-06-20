from django.shortcuts import render, redirect


from datastructures import User, ListaUsuarios, NodeUser
# Create your views here.

def index(request):
    return render(request, 'myAuth/index.html', {})

def register(request):
    user: User = None
    try:
        if request.method == "POST":
            if( request.POST.get('name') is None and request.POST.get('lastName') is None and request.POST.get('email') is None and request.POST.get('password') is None and request.POST.get('phone') is None):
                pass
            else:
                name = request.POST.get('name')
                lastName = request.POST.get('lastName')
                email = request.POST.get('email')
                password = request.POST.get('password')
                phone = request.POST.get('phone')
                user = User( name, lastName, phone, email, password, "cliente" )
    except:
        return render( request, "myAuth/register.html", {
            "error_message": "Ocurrio un problema, vuelve a registrarte"
        })
    else:  
        if user is not None:
            nodeuser: NodeUser = NodeUser( user )
            ok = ListaUsuarios.push( nodeuser )
        
            if ok is not True:
                return render( request, "myAuth/register.html", {
                    "error_message": "Ocurrio un problema, vuelve a registrarte",
                })

            if ok is True:
                return render( request, "myAuth/register.html", {
                    "success_message": "Usuario almacenado Correctamente",
                })
    return render(request, 'myAuth/register.html', {})

def login(request):
    try:
        ok = True
        user = None
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
        
            user, ok = ListaUsuarios.findToValidate( email, password )
    except:
        return render( request, "myAuth/login.html", {
            "error_message": "Ocurrio un problema, vuelve a iniciar sesión"
        })
    else:
        
        if ok is not True:
            return render( request, "myAuth/login.html", {
                "error_message": "Correo o contraseña incorrectos",
                "user": user,
                "ok": ok
            })
        
        if user is not None:
            if user.rol == "administrador":
                request.session['name'] = user.name
                request.session['lastName'] = user.lastName
                return redirect('myAdmin:index')
            else:
                return render( request, "myAuth/login.html", {
                    "success_message": "usuario cliente"
                })
                
    return render(request, 'myAuth/login.html', {})