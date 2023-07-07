from django.urls import path
from .views import *

urlpatterns = [
	path('detalle/<int:id>/<str:slug>', productos_detalle, name="productos_detalle"),
	path('detalle_repuesto/<int:id>/<str:slug>', productos_detalle_repuesto, name="productos_detalle_repuesto"),
	path('tienda-vehiculos/', tiendaVehiculos, name='tiendaVehiculos'),
	path('tienda-vehiculos-por-categoria/<str:slug>', tiendaVehiculos_productos_por_categoria, name='tiendaVehiculos_productos_por_categoria'),
	path('tienda-repuestos/', tiendaRepuestos, name='tiendaRepuestos'),
	path('tienda-repuestos-por-categoria/<str:slug>', tiendaRepuestos_productos_por_categoria, name='tiendaRepuestos_productos_por_categoria'),

]