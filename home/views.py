from django.shortcuts import render
from home.models import *
from utilidades import utilidades

from django.conf import settings


def home_inicio(request):
    datos = Producto.objects.filter(estado_id=1, producto_categoria_id=1).order_by('-id').all()[:8]
    datos2 = Producto.objects.filter(estado_id=1, producto_categoria_id=2).order_by('-id').all()[:8]
    modelo = Producto.objects.filter(estado_id=1, producto_categoria_id=2).order_by('-id').all()

    categorias=VehiculoCategoria.objects.all()
    
    categorias2=VehiculoCategoria.objects.all()

    

    return render(request, 'home/home.html', {'datos': datos, 'datos2': datos2,'categorias': categorias})


