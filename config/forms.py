from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class RegistroForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('username', 'password', 'num_cliente', 'direccion', 'num_telefono', 'correo')
