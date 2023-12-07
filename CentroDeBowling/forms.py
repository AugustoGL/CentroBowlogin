from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva, Cliente

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['dia_reserva', 'hora_reserva']

class RegistroForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('num_cliente', 'direccion', 'num_telefono', 'correo')
