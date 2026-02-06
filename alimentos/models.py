from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nombre = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    fecha_caducidad = models.DateField()
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="alimentos"
    )

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_compra = models.DateField(default=date.today)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    pasos = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo