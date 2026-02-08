from django import forms
from .models import *

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        exclude = ['usuario']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        # ¡AQUÍ AGREGAMOS EL CAMPO!
        fields = ['nombre', 'fecha_compra', 'categoria'] 
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. Leche Entera'
            }),
            'fecha_compra': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos', 'imagen']