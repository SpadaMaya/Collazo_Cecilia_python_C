from django import forms
from .models import Productos

#formulario 
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'fecha_registro', 'estatus']

        def clean(self):
            clean_data = super().clean()
            nombre = clean_data.get('nombre')
            descripcion = clean_data.get('descripcion')
            precio = clean_data.get('precio')
            fecha_registro = clean_data.get('fecha')
            estatus = clean_data.get('estatus')

            if not nombre or not descripcion or not precio or not fecha_registro or not estatus:
                raise forms.ValidationError('Todos los campos deben ser llenados.')
            
            return clean_data

