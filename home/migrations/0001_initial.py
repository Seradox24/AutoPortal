# Generated by Django 4.2.1 on 2023-06-18 02:59

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'db_table': 'genero',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'marca',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(default='0')),
                ('correo', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Metadata',
                'verbose_name_plural': 'Metadata',
                'db_table': 'metadata',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('marca', models.ForeignKey(default='Sin marca', on_delete=django.db.models.deletion.CASCADE, to='home.marca')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'db_table': 'modelo',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_ws', models.CharField(default='0', max_length=255)),
                ('tarjeta', models.CharField(default='0', max_length=10)),
                ('fecha_transbank', models.CharField(default='0', max_length=100)),
                ('estado_transbank', models.CharField(default='0', max_length=100)),
                ('suma', models.PositiveIntegerField(default=0)),
                ('direccion', models.TextField(default='0')),
                ('observaciones', models.TextField(default='')),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('comuna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.comuna')),
                ('estado', models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='home.estado')),
            ],
            options={
                'verbose_name': 'Orden de compra',
                'verbose_name_plural': 'Órdenes de compra',
                'db_table': 'orden_de_compra',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'db_table': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(default='', max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('descripcion', models.TextField(default='')),
                ('adiccional', models.TextField(default='')),
                ('fecha', models.DateField(auto_now=True)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('precio_antes', models.PositiveIntegerField(default=0)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sku', models.CharField(blank=True, default='1', max_length=100, null=True)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('foto', models.ImageField(default='200_200.png', upload_to='producto')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Producto Categoría',
                'verbose_name_plural': 'Productos Categorías',
                'db_table': 'producto_categoria',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Región',
                'verbose_name_plural': 'Región',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('tipo_parte', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=50)),
                ('num_repuesto', models.CharField(max_length=50)),
                ('dimension', models.CharField(max_length=50)),
                ('peso_unitario', models.CharField(max_length=50)),
                ('hecho_en', models.CharField(max_length=50)),
                ('modelo_adecuado', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(default='default-slug', editable=False, populate_from='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='edificacion.png', upload_to='slide')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('target', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slide',
                'db_table': 'slide',
            },
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
            name='VehiculoCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Vehiculo Categoría',
                'verbose_name_plural': 'Vehiculos Categorías',
                'db_table': 'vehiculo_categoria',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_articulo', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
                ('condicion', models.CharField(blank=True, choices=[('NUEVO', 'Nuevo'), ('USADO', 'Usado')], max_length=20, null=True)),
                ('volumen_motor', models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5')], max_length=20)),
                ('volante', models.CharField(choices=[('IZQUIERDA', 'Izquierda'), ('DERECHA', 'Derecha')], max_length=20)),
                ('transmision', models.CharField(choices=[('MECANICA', 'Mecánica'), ('AUTOMATICA', 'Automática')], max_length=20)),
                ('tipo_combustible', models.CharField(choices=[('DIESEL', 'Diesel'), ('GASOLINA', 'Gasolina'), ('ELECTRICO', 'Eléctrico'), ('HIBRIDO', 'Híbrido')], max_length=10)),
                ('num_pasajeros', models.IntegerField()),
                ('puertas', models.IntegerField(choices=[(2, '2 puertas'), (3, '3 puertas'), (4, '4 puertas'), (5, '5 puertas')])),
                ('num_vin', models.CharField(max_length=100)),
                ('color_exterior', models.CharField(choices=[('ROJO', 'Rojo'), ('AZUL', 'Azul'), ('BLANCO', 'Blanco'), ('NEGRO', 'Negro'), ('PLATEADO', 'Plateado')], max_length=20)),
                ('costo_reserva', models.IntegerField(default=0)),
                ('marca', models.ForeignKey(default='Valor predeterminado', on_delete=django.db.models.deletion.DO_NOTHING, to='home.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.modelo')),
                ('tipo_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.vehiculocategoria')),
            ],
        ),
        migrations.CreateModel(
            name='UsersMetadata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios')),
                ('comuna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.comuna')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.estado')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.pais')),
                ('perfiles', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.perfiles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User metadata',
                'verbose_name_plural': 'User metadata',
                'db_table': 'users_metadata',
            },
        ),
        migrations.CreateModel(
            name='ProductoRecomendados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.producto')),
            ],
            options={
                'verbose_name': 'Producto recomendados',
                'verbose_name_plural': 'Productos recomendados',
                'db_table': 'producto_recomendados',
            },
        ),
        migrations.CreateModel(
            name='ProductoFotos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='200_200.png', upload_to='producto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.producto')),
            ],
            options={
                'verbose_name': 'Producto fotos',
                'verbose_name_plural': 'Productos fotos',
                'db_table': 'producto_fotos',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='producto_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.productocategoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.proveedor'),
        ),
        migrations.AddField(
            model_name='producto',
            name='repuesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.repuesto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.sucursal'),
        ),
        migrations.AddField(
            model_name='producto',
            name='vehiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.vehiculo'),
        ),
        migrations.CreateModel(
            name='OrdenDeCompraDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.ordendecompra')),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.producto')),
            ],
            options={
                'verbose_name': 'Orden de compra detalle',
                'verbose_name_plural': 'Órdenes de compra detalle',
                'db_table': 'orden_de_compra_detalle',
            },
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='users_metadata',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.usersmetadata'),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('users_metadata', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.usersmetadata')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contacto', models.CharField(choices=[('TELEFONO', 'Teléfono'), ('EMAIL', 'Email'), ('DIRECCION', 'Dirección')], max_length=10)),
                ('valor_contacto', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='home.usersmetadata')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.region'),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.producto')),
                ('users_metadata', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.usersmetadata')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carrito',
                'db_table': 'carrito',
            },
        ),
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aprobacion', models.DateTimeField(blank=True, null=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aprobaciones', to='home.documento')),
                ('vendedor', models.ForeignKey(limit_choices_to={'tipo_usuario': 'VENDEDOR'}, on_delete=django.db.models.deletion.CASCADE, to='home.usersmetadata')),
            ],
        ),
    ]
