from django.contrib import admin
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', home, name = 'home'),
    path('signup/',signup,  name = 'signup'),
    path('reserva/',reserva,  name = 'reserva'),
    path('reserva/create/',create_reserva,  name = 'create_reserva'),
    path('logout/',logout_view,  name = 'logout'),
    path('login/',login_view,  name = 'login'),
]