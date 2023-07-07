from django.contrib import admin
from django.contrib.admin import AdminSite
from home.models import *
from utilidades import formularios
from PyPDF2 import PdfReader
from django.urls import reverse
from django.utils.html import format_html




# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_articulo')
    search_fields = ('id', 'numero_articulo')


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class PerfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class UsersMetadataAdmin(admin.ModelAdmin):

    list_display = ('id', 'correo', 'telefono', 'direccion', formularios.set_estado, formularios.set_genero, formularios.set_pais, formularios.set_perfiles, formularios.set_user, formularios.set_correo)
    search_fields = ('id', 'pasaporte', 'correo', 'telefono', 'direccion', 'avatar', 'fecha_nacimiento')
    list_per_page = 20


###Productos
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre', 'slug')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', formularios.set_producto_categoria, formularios.set_estado, 'nombre',  formularios.get_descripcion, formularios.get_foto_producto,formularios.get_descripcion, 'stock','precio')
    search_fields = ('id', 'nombre', 'descripcion')  # Corrección aquí
    list_per_page = 20



class ProductoFotosAdmin(admin.ModelAdmin):
    list_display = ('id', formularios.set_producto, formularios.get_foto_producto_galeria)
    list_per_page = 20





class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantidad', formularios.set_users_metadata, formularios.set_producto, 'fecha')
    #search_fields = ('id', 'nombre', 'slug')

class MetadataAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'keyword', 'description', 'correo', 'telefono')
    search_fields = ('id', 'nombre')

 

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Perfiles, PerfilesAdmin)
admin.site.register(UsersMetadata, UsersMetadataAdmin)
admin.site.register(ProductoCategoria, ProductoCategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
#admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Metadata, MetadataAdmin)

class ProductoFotosAdmin(admin.ModelAdmin):
    list_display = ('id', formularios.set_producto, formularios.get_foto_producto_galeria)
    list_per_page = 20

# Registra el modelo ProductoFotos junto con la clase ProductoFotosAdmin
admin.site.register(ProductoFotos, ProductoFotosAdmin)


admin.site.site_header = 'Administración Tienda'
admin.site.index_title = 'Administración Tienda'
admin.site.site_title = 'Administración Tienda'
admin.site.register(Vehiculo)
admin.site.register(Repuesto)
admin.site.register(Sucursal)
admin.site.register(Contacto)


class AprobacionAdmin(admin.ModelAdmin):
    list_display = ['documento', 'vendedor', 'fecha_revision', 'aprobado', 'ver_documento']
    list_filter = ['aprobado']
    search_fields = ['documento__nombre', 'vendedor__nombre']

    def ver_documento(self, obj):
        if obj.documento.archivo:
            documento_url = obj.documento.archivo.url
            return format_html('<a href="{}" target="_blank">Ver Documento</a>', documento_url)
        return "N/A"

    ver_documento.short_description = 'Documento'

admin.site.register(Aprobacion, AprobacionAdmin)

class DocumentoAdmin(admin.ModelAdmin):
    
    list_display = ['nombre', 'archivo', ]


admin.site.register(Documento, DocumentoAdmin)


admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(VehiculoCategoria)
admin.site.register(RepuestoCategoria)

