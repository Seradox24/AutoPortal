from django.shortcuts import render
from home.models import *
from utilidades import utilidades
# Create your views here.
def home_inicio(request):
	#select * from productos where estado_id=1 order by id desc limit 8
	datos=Producto.objects.filter(estado_id=1, producto_categoria_id=1).order_by('-id').all()[:8]
	datos2=Producto.objects.filter(estado_id=1, producto_categoria_id=2).order_by('-id').all()[:8]
	return render(request, 'home/home.html',{'datos':datos,'datos2':datos2})# {'datos':datos})

