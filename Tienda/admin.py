from django.contrib import admin

# Register your models here.
from .models import Usuario, Vehiculo, Repuesto

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Repuesto)