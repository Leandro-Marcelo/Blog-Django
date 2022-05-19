from django.shortcuts import render, redirect
# el authenticate verifica que el username y password sean correctos y luego el login es quien va a guardar el usuario a la session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# IntegrityError significa que la integridad de la base de datos se esta rompiendo, como por ejemplo de que un username que estamos intentando registrar, ya esta registrado
from django.db import IntegrityError


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # User.objects.create_user("tzuzul2","prueba@email.com","123456")

        # Valida las credenciales. Si no existe el usuario el valor es None
        user = authenticate(request, username=username, password=password)

        # eso significa que si existe el usuario
        if user is not None:
            # tambien verificamos si el usuario tiene una cuenta para poder trabajar, o sea que su cuenta ya fue eliminada o algo asi, es otra forma de tambien verificarlo
            if user.is_active:
                # Agregar al usuario a la sesión
                login(request, user)
                return redirect("/")
            else:
                # el segundo parametro es el context, el cual es un diccionario
                return render(request, 'auth/login.html', {
                    "error": True,
                    "message": "Disabled account"
                })
        else:
            return render(request, 'auth/login.html', {
                "error": True,
                "message": "Invalid credentials"
            })

    return render(request, 'auth/login.html')


def user_signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        if password_confirmation != password:
            return render(request, "auth/signup.html", {
                "error": True,
                "message": "Password and password confirmation does not match"
            })

        try:
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            login(request, new_user)
            return redirect("/")

        except IntegrityError:
            return render(request, "auth/signup.html", {
                "error": True,
                "message": "Email or username already registered"
            })

    return render(request, "auth/signup.html")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect("/")
