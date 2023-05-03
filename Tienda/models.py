# Importar la biblioteca ORM de Django
from django.db import models


# Definir una clase que represente la tabla "Usuarios"
class Usuario(models.Model):
    # Definir las opciones para el tipo de usuario
    TIPO_USUARIO = [
        ('VENDEDOR', 'Vendedor'),
        ('ADMINISTRADOR', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('INVITADO', 'Invitado'),
        ('CONTADOR', 'Contador'),
        ('OTRO', 'Otro'),
    ]
    
    # Definir los campos de la tabla "Usuarios"
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    tipo_usuario = models.CharField(max_length=13, choices=TIPO_USUARIO)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    # Opciones para el tipo de combustible
    TIPO_COMBUSTIBLE = [
        ('DIESEL', 'Diesel'),
        ('GASOLINA', 'Gasolina'),
        ('ELECTRICO', 'Eléctrico'),
        ('HIBRIDO', 'Híbrido'),
    ]
    
    # Campos de la tabla "Vehiculos"
    numero_articulo = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    condicion = models.CharField(max_length=20, blank=True, null=True)
    tipo_vehiculo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    volumen_motor = models.CharField(max_length=20)
    volante = models.CharField(max_length=20)
    transmision = models.CharField(max_length=20)
    tipo_combustible = models.CharField(max_length=10, choices=TIPO_COMBUSTIBLE)
    num_pasajeros = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    puertas = models.IntegerField()
    num_vin = models.CharField(max_length=100)
    color_exterior = models.CharField(max_length=20)
    precio_total = models.IntegerField()
    costo_reserva = models.IntegerField()
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.marca + ' ' + self.modelo
    
# Definir una clase que represente la tabla "Repuestos"
class Repuesto(models.Model):
    # Definir los campos de la tabla "Repuestos"
    nombre = models.CharField(max_length=100)
    tipo_parte = models.CharField(max_length=20)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    num_repuesto = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50)
    peso_unitario = models.CharField(max_length=50)
    hecho_en = models.CharField(max_length=50)
    modelo_adecuado = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='repuestos', blank=True, null=True)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='documentos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    
# Definir una clase que represente la tabla "Aprobacion"
class Aprobacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='aprobaciones')
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'VENDEDOR'})
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    aprobado = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.documento.nombre + ' - ' + self.vendedor.nombre