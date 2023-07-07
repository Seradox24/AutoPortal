from django.urls import path
from perfil.views import perfil_inicio, dash_base, dash_editarper, dash_ordenes, dash_admin_repuestos, dash_admin_vehiculo, dash_admin, dash_admin_editar, registrarVehiculo,cambiar_contraseña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', login_required(perfil_inicio), name='perfil_inicio'),
    path('dash_base/', login_required(dash_base), name='dash_base'),
    path('dash_pass/', login_required(cambiar_contraseña), name='cambiar_contraseña'), 
    path('dash_editarper/', login_required(dash_editarper), name='dash_editarper'),
    path('dash_ordenes/', login_required(dash_ordenes), name='dash_ordenes'),
    path('dash_admin_repuestos/', login_required(dash_admin_repuestos), name='dash_admin_repuestos'),
    path('dash_admin_vehiculo/', login_required(dash_admin_vehiculo), name='dash_admin_vehiculo'),
    path('dash_admin/', login_required(dash_admin), name='dash_admin'),
    path('dash_admin_editar/', login_required(dash_admin_editar), name='dash_admin_editar'),
    path('registrarVehiculo/', login_required(registrarVehiculo), name='registrarVehiculo'),
    
]