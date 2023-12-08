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

    def __str__(self):
        return f"Reserva {self.id}"


class Cliente(models.Model):
    num_cliente = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    num_telefono = models.IntegerField()
    correo = models.EmailField()
    listapedidos = models.ManyToManyField('Pedido')

    def crear(self):
        # Implementa la lógica para crear un cliente
        pass

    def hacerReserva(self):
        # Implementa la lógica para hacer una reserva
        pass
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def crear(self):
        # Implementa la lógica para crear un menú
        pass

    def mostrar(self):
        # Implementa la lógica para mostrar el menú
        pass

class ProductoMenu(models.Model):
    precio = models.FloatField()
    productoMenu = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def ActulizarPrecioProducto(self):
        # Implementa la lógica para actualizar el precio del producto
        pass

class Pedido(models.Model):
    descripcion = models.TextField()
    listapedidos = models.ManyToManyField('Pedido')
    hora = models.DateTimeField()

    def crear(self):
        # Implementa la lógica para crear un pedido
        pass

    def cancelar(self):
        # Implementa la lógica para cancelar el pedido
        pass

    def registrarpedido(self):
        # Implementa la lógica para registrar el pedido
        pass

class DetallePedido(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def crear(self):
        # Implementa la lógica para crear un detalle de pedido
        pass

class PrecioProducto(models.Model):
    precio = models.FloatField()
    fecha_vigencia = models.DateField()

    def verificarPrecioProducto(self):
        # Implementa la lógica para verificar el precio de un producto
        pass

class AsignacionPedido(models.Model):
    descripcion = models.TextField()
    precio = models.IntegerField()

    def verificaEleccionPedido(self):
        # Implementa la lógica para verificar la elección de un pedido
        pass

    def obetnerPrecio(self):
        # Implementa la lógica para obtener el precio de la asignación de pedido
        pass

class Partida(models.Model):
    identificador_unico = models.CharField(max_length=50)
    descripcion = models.TextField()

    def crear(self):
        # Implementa la lógica para crear una partida
        pass

    def cancelarPartida(self):
        # Implementa la lógica para cancelar una partida
        pass

    def calcularPuntajeTotal(self):
        # Implementa la lógica para calcular el puntaje total de la partida
        pass

    def calcularCantidadJugadores(self):
        # Implementa la lógica para calcular la cantidad de jugadores en la partida
        pass


