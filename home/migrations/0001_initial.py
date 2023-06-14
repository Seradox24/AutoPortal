# Generated by Django 4.2.1 on 2023-06-05 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('proveedor', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_parte', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=50)),
                ('num_repuesto', models.CharField(max_length=50)),
                ('dimension', models.CharField(max_length=50)),
                ('peso_unitario', models.CharField(max_length=50)),
                ('hecho_en', models.CharField(max_length=50)),
                ('modelo_adecuado', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='repuestos')),
                ('titulo', models.CharField(max_length=100)),
                ('precio_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('VENDEDOR', 'Vendedor'), ('ADMINISTRADOR', 'Administrador'), ('CLIENTE', 'Cliente'), ('INVITADO', 'Invitado'), ('CONTADOR', 'Contador'), ('OTRO', 'Otro')], max_length=13)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_articulo', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
                ('condicion', models.CharField(blank=True, max_length=20, null=True)),
                ('tipo_vehiculo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('volumen_motor', models.CharField(max_length=20)),
                ('volante', models.CharField(max_length=20)),
                ('transmision', models.CharField(max_length=20)),
                ('tipo_combustible', models.CharField(choices=[('DIESEL', 'Diesel'), ('GASOLINA', 'Gasolina'), ('ELECTRICO', 'Eléctrico'), ('HIBRIDO', 'Híbrido')], max_length=10)),
                ('num_pasajeros', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('puertas', models.IntegerField()),
                ('num_vin', models.CharField(max_length=100)),
                ('color_exterior', models.CharField(max_length=20)),
                ('costo_reserva', models.IntegerField(default=0)),
                ('titulo', models.CharField(default='', max_length=100)),
                ('precio_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.vehiculo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ingreso')),
                ('repuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.repuesto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.factura')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contacto', models.CharField(choices=[('TELEFONO', 'Teléfono'), ('EMAIL', 'Email'), ('DIRECCION', 'Dirección')], max_length=10)),
                ('valor_contacto', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='home.usuario')),
                ('vehiculos', models.ManyToManyField(to='home.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aprobacion', models.DateTimeField(blank=True, null=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aprobaciones', to='home.documento')),
                ('vendedor', models.ForeignKey(limit_choices_to={'tipo_usuario': 'VENDEDOR'}, on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
    ]