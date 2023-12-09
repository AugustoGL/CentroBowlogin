from django.contrib import admin
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', home, name = 'home'),
    path('signup/',signup,  name = 'signup'),
    path('reservar/',reservar,  name = 'reservar'),
    path('reservas/<int:pk>/',reservas,  name = 'reservas'),
    path('reserva/<int:pk>/',reserva,  name = 'reserva'),
    path('logout/',logout_view,  name = 'logout'),
    path('login/',login_view,  name = 'login'),
]