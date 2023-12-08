from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from datetime import datetime


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
                print(user.pk, "--------"*10)
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
    horarios = Horarios.objects.all()
    if request.method == 'POST':
        print("POST"*8)
        dia_reserva = request.POST.get('dia_reserva')
        hora_reserva_id = request.POST.get('hora_reserva')
        nombres_personas = request.POST.getlist('nombre_persona[]')
        codigos_personas = request.POST.getlist('codigo_persona[]')

       
        fecha_reserva = datetime.strptime(dia_reserva, '%Y-%m-%d').date()
        pista = Pista.objects.filter(estado__estado='Disponible').first()
        if not pista:
            return render(request, 'rev.html', {'horarios': horarios,})
        print("arranca","*********"*5)
        usuario = User.objects.get(id=request.user.pk)
        reserva = Reserva.objects.create(
            usuario=usuario,
            dia_reserva=fecha_reserva,
            hora_reserva=Horarios.objects.get(id=hora_reserva_id),
            pista=pista
        )
        print("o no arranca")
        for nombre, codigo in zip(nombres_personas, codigos_personas):
            jugador = Jugador.objects.create(nombre=nombre, resumido=codigo)
            reserva.jugadores.add(jugador)

        pista.estado = EstadoPista.objects.get(estado='Reservada')
        pista.save()

        return render(request, 'home.html')
    else:
       return render(request, 'rev.html', {'horarios': horarios})


    


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