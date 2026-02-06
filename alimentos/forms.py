from django import forms
from .models import *

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nombre', 'fecha_compra']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos', 'imagen']