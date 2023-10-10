from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                #login(request, user)
                return redirect('/users/signin')
            except IntegrityError:
                return render(request, 'users/signup.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'users/signup.html', {"form": UserCreationForm, "error": "La clave no coincide."})


def signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/signin.html', {"form": AuthenticationForm, "error": "Usuario o clave incorrecto."})

        login(request, user)
        return redirect('/')

        
       
def logout_view(request):
    logout(request)
    return redirect('/')  
    
