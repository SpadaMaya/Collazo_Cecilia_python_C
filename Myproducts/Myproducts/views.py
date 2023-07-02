from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json
def insertar_producto(request):
    # Código de la vista
    return HttpResponse("Insertar producto")


def index(request):

    return HttpResponse('Hola Mundo')

class Inicio(View):
    teamplate_name = 'index.html'

    def post():

        return
    
    def get(self, request):

        return render(request, self.teamplate_name)