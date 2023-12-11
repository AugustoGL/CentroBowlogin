from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['dia_reserva', 'hora_reserva']

