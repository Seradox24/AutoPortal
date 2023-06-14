from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from datetime import datetime, date
from django.utils.text import slugify

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'



class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'genero'
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'perfiles'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'region'
        verbose_name = 'Región'
        verbose_name_plural = 'Región'


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, default=1)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'comuna'
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'


class UsersMetadata(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    estado = models.ForeignKey(Estado, models.DO_NOTHING)
    genero = models.ForeignKey(Genero, models.DO_NOTHING)
    perfiles = models.ForeignKey(Perfiles, models.DO_NOTHING)
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, default=1)
    slug = models.CharField(max_length=100, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'users_metadata'
        verbose_name = 'User metadata'
        verbose_name_plural = 'User metadata'

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class ProductoCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto_categoria'
        verbose_name = 'Producto Categoría'
        verbose_name_plural = 'Productos Categorías'


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=100, default='')
    slug = AutoSlugField(populate_from='nombre')
    descripcion = models.TextField(default='')
    adiccional = models.TextField(default='')
    producto_categoria = models.ForeignKey('ProductoCategoria', on_delete=models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.DO_NOTHING, default=1)
    estado = models.ForeignKey('Estado', on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_now=True)
    precio = models.PositiveIntegerField(default=0)
    precio_antes = models.PositiveIntegerField(default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sku = models.CharField(max_length=100, blank=True, null=True, default='1')
    stock = models.PositiveIntegerField(default=1)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, null=True, blank=True)
    repuesto = models.ForeignKey('Repuesto', on_delete=models.CASCADE, null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    foto=models.ImageField(upload_to="producto", default='200_200.png')


    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Vehiculo(models.Model):
    # Opciones para la condición del vehículo
    CONDICION_CHOICES = [
        ('NUEVO', 'Nuevo'),
        ('USADO', 'Usado'),
    ]

    # Opciones para el tipo de vehículo
    TIPO_VEHICULO_CHOICES = [
        ('SEDAN', 'Sedán'),
        ('SUV', 'SUV'),
        ('CAMIONETA', 'Camioneta'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupé'),
    ]

    # Opciones para el volumen del motor
    VOLUMEN_MOTOR_CHOICES = [
        ('1.0', '1.0'),
        ('1.5', '1.5'),
        ('2.0', '2.0'),
        ('2.5', '2.5'),
    ]

    # Opciones para la ubicación
    UBICACION_CHOICES = [
        ('IQUIQUE', 'Iquique'),
        ('ALTO HOSPICIO', 'Alto Hospicio'),
        ('OTRO', 'Otro'),
    ]

    # Opciones para el número de puertas
    PUERTAS_CHOICES = [
        (2, '2 puertas'),
        (4, '4 puertas'),
        (5, '5 puertas'),
    ]

    # Opciones para el color exterior
    COLOR_EXTERIOR_CHOICES = [
        ('ROJO', 'Rojo'),
        ('AZUL', 'Azul'),
        ('BLANCO', 'Blanco'),
        ('NEGRO', 'Negro'),
        ('PLATEADO', 'Plateado'),
    ]
    TIPO_COMBUSTIBLE = [
        ('DIESEL', 'Diesel'),
        ('GASOLINA', 'Gasolina'),
        ('ELECTRICO', 'Eléctrico'),
        ('HIBRIDO', 'Híbrido'),
    ]

    # Opciones para el tipo de volante
    TIPO_VOLANTE = [
        ('IZQUIERDA', 'Izquierda'),
        ('DERECHA', 'Derecha'),
    ]

    # Opciones para el tipo de transmisión
    TIPO_TRANSMISION = [
        ('MECANICA', 'Mecánica'),
        ('AUTOMATICA', 'Automática'),
    ]

    # Campos de la tabla "Vehiculos"
    numero_articulo = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    condicion = models.CharField(max_length=20, choices=CONDICION_CHOICES, blank=True, null=True)
    tipo_vehiculo = models.CharField(max_length=20, choices=TIPO_VEHICULO_CHOICES)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    volumen_motor = models.CharField(max_length=20, choices=VOLUMEN_MOTOR_CHOICES)
    volante = models.CharField(max_length=20,choices=TIPO_VOLANTE)
    transmision = models.CharField(max_length=20)
    tipo_combustible = models.CharField(max_length=10, choices=TIPO_COMBUSTIBLE)
    num_pasajeros = models.IntegerField()
    puertas = models.IntegerField(choices=PUERTAS_CHOICES)
    num_vin = models.CharField(max_length=100)
    color_exterior = models.CharField(max_length=20, choices=COLOR_EXTERIOR_CHOICES)
    costo_reserva = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, default=1)

    def __str__(self):
        return self.marca + ' ' + self.modelo


class Repuesto(models.Model):
    tipo_parte = models.CharField(max_length=20)
    categoria = models.CharField(max_length=50)
    num_repuesto = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50)
    peso_unitario = models.CharField(max_length=50)
    hecho_en = models.CharField(max_length=50)
    modelo_adecuado = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, default=1)
    slug = AutoSlugField(populate_from='nombre', default='default-slug')
    
    def __str__(self):
        return self.nombre



class ProductoFotos(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    foto=models.ImageField(upload_to="producto", default='200_200.png')

    def __str__(self):
        return self.producto.nombre

    class Meta:
        db_table = 'producto_fotos'
        verbose_name = 'Producto fotos'
        verbose_name_plural = 'Productos fotos'


class ProductoRecomendados(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        db_table = 'producto_recomendados'
        verbose_name = 'Producto recomendados'
        verbose_name_plural = 'Productos recomendados'

class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200,default='')
    archivo = models.FileField(upload_to='documentos/')
    users_metadata = models.ForeignKey(UsersMetadata, models.DO_NOTHING, default=1, related_name='documentos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    users_metadata = models.ForeignKey(UsersMetadata, models.DO_NOTHING, default=1)
    def __str__(self):
        return self.nombre


class Aprobacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='aprobaciones')
    vendedor = models.ForeignKey(UsersMetadata, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'VENDEDOR'})
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    aprobado = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.documento.nombre + ' - ' + self.vendedor.nombre


class Contacto(models.Model):
    TIPO_CONTACTO = [
        ('TELEFONO', 'Teléfono'),
        ('EMAIL', 'Email'),
        ('DIRECCION', 'Dirección'),
    ]

    usuario = models.ForeignKey(UsersMetadata, on_delete=models.CASCADE, related_name='contactos')
    tipo_contacto = models.CharField(max_length=10, choices=TIPO_CONTACTO)
    valor_contacto = models.CharField(max_length=100)

    def __str__(self):
        return f"Contacto de {self.usuario.nombre}: {self.tipo_contacto} - {self.valor_contacto}"





class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    foto=models.ImageField(upload_to="slide", default='edificacion.png')
    link = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    target = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'slide'
        verbose_name = 'Slide'
        verbose_name_plural = 'Slide'



####carrito
class Carrito(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, default=1)
	users_metadata = models.ForeignKey(UsersMetadata, on_delete=models.DO_NOTHING, default=1)
	cantidad = models.PositiveIntegerField(default=0)
	fecha = models.DateField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return f"{self.producto.nombre}"


	class Meta:
		db_table = 'carrito'
		verbose_name = 'Carrito'
		verbose_name_plural = 'Carrito'


class OrdenDeCompra(models.Model):
    users_metadata = models.ForeignKey(UsersMetadata, models.DO_NOTHING, default=1)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, default=3)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, default=1)
    token_ws = models.CharField(max_length=255, default='0')
    tarjeta = models.CharField(max_length=10, default='0')
    fecha_transbank = models.CharField(max_length=100, default='0')
    estado_transbank = models.CharField(max_length=100, default='0')
    suma = models.PositiveIntegerField(default=0)
    direccion = models.TextField(default='0')
    observaciones = models.TextField(default='')
    fecha = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"N°{self.id}"


    class Meta:
        db_table = 'orden_de_compra'
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Órdenes de compra'


class OrdenDeCompraDetalle(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, models.DO_NOTHING)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, default=1)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"N°{self.id}"


    class Meta:
        db_table = 'orden_de_compra_detalle'
        verbose_name = 'Orden de compra detalle'
        verbose_name_plural = 'Órdenes de compra detalle'



####metadata
class Metadata(models.Model):
    keyword = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(default='0')
    correo = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.correo

    class Meta:
        db_table = 'metadata'
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadata'