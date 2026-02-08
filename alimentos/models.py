from django.db import models
from datetime import date
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="alimentos"
    )

    nombre = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    fecha_caducidad = models.DateField()
    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='alimentos/')

    def estado(self):
        hoy = timezone.now().date()

        if self.fecha_caducidad < hoy:
            return "rojo"
        elif self.fecha_caducidad <= hoy + timedelta(days=3):
            return "amarillo"
        else:
            return "verde"

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    # Tu lista personalizada de categorías
    CATEGORIAS_CHOICES = [
        ('FRUTAS', '🍎 Frutas y verduras'),
        ('CARNES', '🥩 Carnes y proteínas'),
        ('LACTEOS', '🥛 Lácteos'),
        ('CEREALES', '🌾 Cereales y granos'),
        ('ENLATADOS', '🥫 Enlatados y conservas'),
        ('ESPECIAS', '🧂 Condimentos y especias'),
        ('SNACKS', '🍪 Snacks'),
        ('CONGELADOS', '❄️ Congelados'),
        ('BEBIDAS', '🧃 Bebidas'),
        ('OTROS', '📦 Otros'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="compras"
    )
    nombre = models.CharField(max_length=100)
    fecha_compra = models.DateField(default=date.today)
    comprado = models.BooleanField(default=False)
    
    
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_CHOICES,
        default='OTROS'
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"

    
class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    pasos = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)

    def __str__(self):
        return self.titulo