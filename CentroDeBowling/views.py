from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from datetime import datetime
from django.http import HttpResponse
from django.db import IntegrityError

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


def reservas(request, pk):
    reservas = Reserva.objects.filter(usuario=pk)
    print(reservas)
    for jugadores in reservas:
        print(jugadores.jugadores.all())
    return render(request, 'reservas.html', {'reservas': reservas}) 

def reservar(request):
    if request.method == 'POST':
        print("POST" * 8)
        dia_reserva = request.POST.get('dia_reserva')
        hora_reserva_id = request.POST.get('hora_reserva')
        nombres_personas = request.POST.getlist('nombre_persona[]')
        codigos_personas = request.POST.getlist('codigo_persona[]')

        fecha_reserva = datetime.strptime(dia_reserva, '%Y-%m-%d').date()


        
        pista_disponible = Pista.objects.filter(
            estado__estado='Disponible',
        ).first()

        """""""""
        if not pista_disponible:
            return HttpResponse('No hay pistas disponibles')
        """""""""
        
        usuario = User.objects.get(id=request.user.pk)
        
        # Capturar excepciones de integridad para manejar casos en los que la transacción falle
        try:
            reserva = Reserva.objects.create(
                usuario=usuario.pk,
                dia_reserva=fecha_reserva,
                hora_reserva=Horarios.objects.get(id=hora_reserva_id),
                pista=pista_disponible
            )
            
            for nombre, codigo in zip(nombres_personas, codigos_personas):
                jugador = Jugador.objects.create(nombre=nombre, resumido=codigo)
                reserva.jugadores.add(jugador)
            """""""""
            pista_disponible.estado = EstadoPista.objects.get(estado='Reservada', horario__id=hora_reserva_id)
            pista_disponible.save()
            """""""""
        except IntegrityError:
            # Manejar la excepción, por ejemplo, mostrar un mensaje de error o redirigir a una página de error
            return HttpResponse('Error al crear la reserva')

        return redirect('reservas', pk=usuario.pk)
    else:
        horarios = Horarios.objects.all()
        return render(request, 'reservar.html', {'horarios': horarios})

def reserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    usuario = User.objects.get(id=reserva.usuario)
    pedidos = Pedido.objects.filter(reserva=pk) 
    if request.method == 'POST':
        reserva.estado_reserva = EstadoReserva.objects.get(pk=2)
        reserva.save()
    return render(request, 'reserva.html', {'reserva': reserva, 'usuario': usuario, 'pedidos': pedidos})


def pedir(request, pk):
    reservas = Reserva.objects.filter(usuario=pk)
    productos = Producto.objects.all()

    if request.method == 'POST':
        reserva_id = request.POST.get('reserva_id')
        reserva = Reserva.objects.get(id=reserva_id)
        pedido = Pedido.objects.create(reserva=reserva)
        for producto in productos:
            producto_pk = str(producto.pk)
            cantidad = request.POST.get('producto_' + producto_pk)
            if cantidad and cantidad != '0':
                detalles_pedido = detallesPedido.objects.create(
                    cantidad=cantidad,
                    producto=producto
                )
                pedido.detalles.add(detalles_pedido)
        return redirect('reserva', pk=reserva_id)
    return render(request, 'pedir.html', {'reservas': reservas, 'productos': productos})


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
            return redirect('reservar')
        



def logout_view(request):
    logout(request)
    return redirect('home')