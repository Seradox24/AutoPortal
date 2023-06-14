from django.urls import path
from .views import *

urlpatterns = [
	path('detalle/<int:id>/<str:slug>', productos_detalle, name="productos_detalle"),
	path('detalle_repuesto/<int:id>/<str:slug>', productos_detalle_repuesto, name="productos_detalle_repuesto"),
	
	
]