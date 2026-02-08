from django.contrib import admin
from .models import Alimento, Categoria, Compra, Receta 

admin.site.register(Alimento)
admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Receta)