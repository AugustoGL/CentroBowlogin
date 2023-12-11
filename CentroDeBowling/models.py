from django.db import models



class Horarios(models.Model):
    horario = models.TimeField()

    def __str__(self):
        return str(self.horario)

class EstadoPista(models.Model):
    estado = models.CharField(max_length=100, default="Disponible")
    horario = models.ForeignKey('Horarios', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"{self.horario} - {self.estado}"


class EstadoReserva(models.Model):
    estado = models.CharField(max_length=100, default="Reservada")

    def __str__(self):
        return self.estado

class Pista(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey(EstadoPista, on_delete=models.CASCADE, default=1)  # Cambia el valor por el ID correcto

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    resumido = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.IntegerField(default=0)
    dia_reserva = models.DateField()
    hora_reserva = models.ForeignKey(Horarios, on_delete=models.CASCADE)
    jugadores = models.ManyToManyField(Jugador)
    pista = models.ForeignKey(Pista, on_delete=models.CASCADE)
    estado_reserva = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return f"Reserva {self.id}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def actualizar_precio_producto(self, nuevo_precio):
        self.precio = nuevo_precio
        self.save()

    def __str__(self):
        return self.nombre

class detallesPedido(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def calcularTotal(self):
        total_detalles = self.cantidad * self.producto.precio
        return total_detalles
    
    def __str__(self):
        return f"{self.cantidad} {self.producto.nombre}"


class Pedido(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    detalles = models.ManyToManyField(detallesPedido)


    def calcularTotal(self):
        total_pedido = 0
        for detalle in self.detalles.all():
            total_pedido += detalle.calcularTotal()
        return total_pedido
    
    def detallesPedido(self):
        return self.detalles.all()
    
    def __str__(self):
        return f"Pedido {self.id}"