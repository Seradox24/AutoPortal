from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('core/backend/', admin.site.urls, name="backend"),
    path('', include('home.urls'),name="home_urls"),
    path('acceso/', include('acceso.urls'),name="acceso_urls"),
    path('productos/', include('productos.urls'),name="productos_urls"),
    path('carro/', include('carro.urls'),name="carro_urls"),
    path('perfil/', include('perfil.urls')),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

