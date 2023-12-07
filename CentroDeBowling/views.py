from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('reserva')
            except IntegrityError:
                return render (request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existente'
                })
        return render (request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contra no coinciden'
        })


def reserva(request):
    return render(request, 'rev.html')

def create_reserva(request):
    if request.method == 'GET':
        return render(request, 'c_rev.html',{
        'form': ReservaForm
    })
    else:
        try:
            form = ReservaForm(request.POST)
            new_reserva = form.save(commit=False)
            new_reserva.user = request.user
            new_reserva.save()
            return redirect('reserva')
        except ValueError:
            return render(request, 'c_rev.html',{
                'form': ReservaForm,
                "error": 'Datos no validos'
            })

    


def login_view(request):
    if request.method == 'GET':
        return render(request,'login.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{
                'form': AuthenticationForm,
                "error": 'Usuario o contra es incorrecto'
            })  
        else:
            login(request, user)
            return redirect('reserva')
        



def logout_view(request):
    logout(request)
    return redirect('home')