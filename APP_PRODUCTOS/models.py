from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField()
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
     usuario = models.OneToOneField(User, on_delete=models.CASCADE)