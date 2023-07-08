from django.db import models

# Create your models here.
class Proveedores(models.Model):
    ruc=models.IntegerField(null=True)
    nombre=models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.ruc} {self.nombre} {self.direccion}'

class Producto(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.nombre} {self.precio}'
class Cliente(models.Model):
    cedula = models.IntegerField(null=True)
    nombre= models.CharField(max_length=20, null=True)
    apellido = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    direccion = models.CharField(max_length=100, null=True)
    telefono = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.cedula} {self.nombre} {self.apellido}'

class Factura (models.Model):
    fecha= models.DateField(null=True)
    cantidad = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    cliente= models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    proveedores = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.fecha} {self.cantidad} {self.total} '



