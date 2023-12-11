from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Reserva)
admin.site.register(Pista)
admin.site.register(Horarios)
admin.site.register(EstadoPista)
admin.site.register(EstadoReserva)
admin.site.register(Jugador)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(detallesPedido)