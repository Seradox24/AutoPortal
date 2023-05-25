from django.shortcuts import render
from .models import Vehiculo

# Create your views here.

def home_inicio(request):
    return render(request,'home/home.html', {} )


# Vista para la página de inicio de sesión
def login_view(request):
    return render(request, 'tienda/login.html')

# Vista para la página de perfil del usuario
def perfil_view(request):
    return render(request, 'tienda/perfil.html')

# Vista para la tienda de autos
def tienda_autos_view(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'tienda/tienda_autos.html', {'vehiculos': vehiculos})

# Vista para la tienda de repuestos
def tienda_repuestos_view(request):
    return render(request, 'tienda/tienda_repuestos.html')

# Vista para el carrito de compras
def carrito_view(request):
    return render(request, 'tienda/carrito.html')

# Vista para la integración con Webpay
def webpay_integration_view(request):
    return render(request, 'tienda/webpay_integration.html')

# Vista para la página "Nosotros"
def nosotros_view(request):
    return render(request, 'tienda/nosotros.html')

# Otras vistas necesarias para tu aplicación