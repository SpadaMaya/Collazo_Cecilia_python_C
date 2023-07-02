from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos
from .forms import ProductoForm

def index(request):

    return HttpResponse('Hola Mundo')

class Inicio(View):
    teamplate_name = 'index.html'

    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')

        return render(request, self.teamplate_name, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()
        form = ProductoForm()
        return render(request, self.teamplate_name, {'form': form,'productos': productos})
    
    def insertar_producto(request):
    # Código de la vista

        ''' nuevo_producto = Productos(
           nombre = 'Mapa1',
           descripcion = 'Tecnica mixta',
           precio = 8000,
           fecha_registro = 20/6/2023,
           estatus = True
        )
        nuevo_producto.save()'''
    

        return HttpResponse('Libro insertado correctamente')