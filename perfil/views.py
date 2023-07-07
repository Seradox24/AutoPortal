from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from home.models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime, date, timedelta
from django.contrib import messages
from utilidades import utilidades, dreamhost

from .forms import EditarUsuarioForm
from django.contrib.auth.forms import PasswordChangeForm




from django.contrib.auth.decorators import login_required

def perfil_inicio(request):
    # Código de la vista perfil_inicio
    return HttpResponse("Página de inicio de perfil")

def dash_base(request):
    user = request.user

    users_metadata = UsersMetadata.objects.get(user=request.user)

    ordenesListados = OrdenDeCompra.objects.filter(users_metadata=users_metadata).order_by('-id')
    
    conteo = ordenesListados.count()
    # Código de la vista dash_base

    categorias=VehiculoCategoria.objects.all()
    

    return render(request, 'perfil/dash_base.html',  {'data': user, 'conteo': conteo,'categorias': categorias})

@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('acceso_login')
    else:
        form = PasswordChangeForm(request.user)
    categorias=VehiculoCategoria.objects.all()
    
    return render(request, 'perfil/dash_pass.html', {'form': form,'categorias': categorias})
    
@login_required
def dash_editarper(request):
    user = request.user  # Obtiene el usuario autenticado
    metadata = user.usersmetadata  # Obtiene la metadata del usuario
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=user)
        form_metadata = UsersMetadataForm(request.POST, instance=metadata)
        if form.is_valid():
            form.save()  # Guarda los cambios en el usuario
            form_metadata.save()  # Guarda los cambios en la metadata

            return redirect('dash_editarper')  # Redirige a la página de perfil o a la que desees
    else:
        form = EditarUsuarioForm(instance=user)
        form_metadata = UsersMetadataForm(instance=metadata)
    # Código de la vista dash_editarper
    categorias=VehiculoCategoria.objects.all()
    
    return render(request, 'perfil/dash_editarper.html',  {'form': form, 'form_metadata': form_metadata,'categorias': categorias})

@login_required
def dash_ordenes(request):
    users_metadata = UsersMetadata.objects.get(user=request.user)

    ordenesListados = OrdenDeCompra.objects.filter(users_metadata=users_metadata).order_by('-id')
    documentosListados = Documento.objects.filter(users_metadata=users_metadata, ordenDeCompra__in=ordenesListados)
    categorias=VehiculoCategoria.objects.all()
    
    context = {
        'ordenesListados': ordenesListados,
        'documentosListados': documentosListados,
        'categorias': categorias
    }
    
    return render(request, 'perfil/dash_ordenes.html', context)


def dash_admin_repuestos(request):
    # Código de la vista dash_ordenes
    return render(request, 'perfil/dash_admin_tb_repuestos.html')

def dash_admin_vehiculo(request):
    # Código de la vista dash_ordenes
    vehiculosListados = Producto.objects.all()
    return render(request, 'perfil/dash_admin_tb_vehiculos.html',{"vehiculos":vehiculosListados})



def dash_admin(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            form.save(commit=True, request=request)
            return redirect('dash_editarper')
    else:
        form = DocumentoForm(user=request.user)
    
    categorias=VehiculoCategoria.objects.all()
    

    return render(request, 'perfil/dash_admin.html', {'form': form,'categorias': categorias})







def dash_admin_editar(request):
    # Código de la vista dash_ordenes
    return render(request, 'perfil/dash_editar.html')





def registrarVehiculo(request):
    print('')
  
    
    return redirect('/')
    





