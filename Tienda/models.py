from django.db import models


class Usuario(models.Model):
    TIPO_USUARIO = [
        ('VENDEDOR', 'Vendedor'),
        ('ADMINISTRADOR', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('INVITADO', 'Invitado'),
        ('CONTADOR', 'Contador'),
        ('OTRO', 'Otro'),
    ]
    
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
    precio_total = models.IntegerField(default=0)
    costo_reserva = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100, default='')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Agregado el campo precio_total
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.marca + ' ' + self.modelo

class Repuesto(models.Model):
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
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)

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


class Aprobacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='aprobaciones')
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'VENDEDOR'})
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    aprobado = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.documento.nombre + ' - ' + self.vendedor.nombre


class Factura(models.Model):
    numero_factura = models.CharField(max_length=100)
    fecha = models.DateField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_factura


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Detalle de factura {self.factura.numero_factura}"


class DetalleVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Detalle de venta del vehículo {self.vehiculo.modelo}"


class Ingreso(models.Model):
    fecha = models.DateField()
    proveedor = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ingreso {self.id}"


class DetalleIngreso(models.Model):
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de ingreso {self.ingreso.id}"


class Contacto(models.Model):
    TIPO_CONTACTO = [
        ('TELEFONO', 'Teléfono'),
        ('EMAIL', 'Email'),
        ('DIRECCION', 'Dirección'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contactos')
    tipo_contacto = models.CharField(max_length=10, choices=TIPO_CONTACTO)
    valor_contacto = models.CharField(max_length=100)

    def __str__(self):
        return f"Contacto de {self.usuario.nombre}: {self.tipo_contacto} - {self.valor_contacto}"


class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')
    vehiculos = models.ManyToManyField(Vehiculo)

    def __str__(self):
        return f"Carrito de {self.usuario.nombre}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
