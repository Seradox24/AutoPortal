from django.shortcuts import render
from home.models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from utilidades import utilidades


def productos_detalle(request, id, slug):

    categorias=VehiculoCategoria.objects.all()
    categorias2=VehiculoCategoria.objects.all()
    try:
        datos=Producto.objects.filter(pk=id).filter(slug=slug).filter(estado_id=1).get()
    except Producto.DoesNotExist:
        raise Http404

    relacionados=Producto.objects.filter(estado_id=1, producto_categoria=datos.producto_categoria_id).filter(estado_id=1).all()
    fotos=ProductoFotos.objects.filter(producto_id=id).all()
    return render(request, 'productos/detalle.html', {'datos':datos, 'relacionados': relacionados, 'fotos': fotos,'categorias': categorias})

def productos_detalle_repuesto(request, id, slug):
    try:
        datos=Producto.objects.filter(pk=id).filter(slug=slug).filter(estado_id=1).get()
    except Producto.DoesNotExist:
        raise Http404
		
    relacionados=Producto.objects.filter(estado_id=1, producto_categoria=datos.producto_categoria_id).filter(estado_id=1).all()
    fotos=ProductoFotos.objects.filter(producto_id=id).all()
    return render(request, 'productos/detalle_repuesto.html', {'datos':datos, 'relacionados': relacionados, 'fotos': fotos})


def tiendaVehiculos(request):
    total=Producto.objects.filter(estado_id=1, producto_categoria_id=1).order_by('-id').all()
    categorias=VehiculoCategoria.objects.all()
    categorias2=VehiculoCategoria.objects.all()
    
    paginar= utilidades.paginacion(total,request)
    page = int(paginar[2]) if paginar[2] is not None else 1
    num_productos = total.count()

   

 



    return render(request, 'tienda/categoriasVehiculos.html',{'datos':paginar[0],'categorias': categorias,'num_productos':num_productos,
    'total':total,'numeros':paginar[1],'page':page})

def tiendaVehiculos_productos_por_categoria(request, slug):
    try:
        cat=VehiculoCategoria.objects.filter(slug=slug).get()
    except VehiculoCategoria.DoesNotExist:
        raise Http404

    total=Producto.objects.filter(estado_id=1, producto_categoria_id=1,vehiculo__tipo_vehiculo_id=cat.id).order_by('-id').all()
    categorias=VehiculoCategoria.objects.all()
    paginar= utilidades.paginacion(total,request)
    page = int(paginar[2]) if paginar[2] is not None else 1
    num_productos = total.count()
    #categorias2=VehiculoCategoria.objects.all()
    #tipo_combustible_list = datos.vehiculo.values_list('tipo_combustible', flat=True).distinct()
    return render(request, 'tienda/tiendaVehiculos_productos_por_categoria.html',{'datos':paginar[0],'cat':cat,'categorias': categorias,'num_productos':num_productos,
    'total':total,'numeros':paginar[1],'page':page})

def tiendaRepuestos(request):
    total=Producto.objects.filter(estado_id=1, producto_categoria_id=2).order_by('-id').all()
    categorias=RepuestoCategoria.objects.all()
    categorias2=RepuestoCategoria.objects.all()
    
    paginar= utilidades.paginacion(total,request)
    page = int(paginar[2]) if paginar[2] is not None else 1
    num_productos = total.count()
    return render(request, 'tienda/categoriasRepuestos.html',{'datos':paginar[0],'categorias': categorias,'num_productos':num_productos,
    'total':total,'numeros':paginar[1],'page':page})
    


def tiendaRepuestos_productos_por_categoria(request, slug):
    try:
        cat=RepuestoCategoria.objects.filter(slug=slug).get()
    except VehiculoCategoria.DoesNotExist:
        raise Http404

    total=Producto.objects.filter(estado_id=1, producto_categoria_id=2,repuesto__tipo_repuesto_id=cat.id).order_by('-id').all()
    categorias=RepuestoCategoria.objects.all()
    paginar= utilidades.paginacion(total,request)
    page = int(paginar[2]) if paginar[2] is not None else 1
    num_productos = total.count()
    #categorias2=VehiculoCategoria.objects.all()
    #tipo_combustible_list = datos.vehiculo.values_list('tipo_combustible', flat=True).distinct()
    return render(request, 'tienda/tiendaRepuestos_productos_por_categoria.html',{'datos':paginar[0],'cat':cat,'categorias': categorias,'num_productos':num_productos,
    'total':total,'numeros':paginar[1],'page':page})
