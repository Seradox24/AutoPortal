
from django.urls import path
from .views import (
    home_inicio,
    login_view,
    perfil_view,
    tienda_autos_view,
    tienda_repuestos_view,
    carrito_view,
    webpay_integration_view,
    nosotros_view,
)

urlpatterns = [
    path('', home_inicio, name='home_inicio'), 
    path('login/', login_view, name='login'),
    path('perfil/', perfil_view, name='perfil'),
    path('tienda/autos/', tienda_autos_view, name='tienda_autos'),
    path('tienda/repuestos/', tienda_repuestos_view, name='tienda_repuestos'),
    path('carrito/', carrito_view, name='carrito'),
    path('webpay/integracion/', webpay_integration_view, name='webpay_integration'),
    path('nosotros/', nosotros_view, name='nosotros'),
    # Agrega más rutas necesarias para tu aplicación
]
