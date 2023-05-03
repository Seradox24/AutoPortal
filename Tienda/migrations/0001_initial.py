# Generated by Django 4.2 on 2023-05-03 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('precio_total', models.IntegerField()),
                ('costo_reserva', models.IntegerField()),
                ('titulo', models.CharField(max_length=100)),
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
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='Tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aprobacion', models.DateTimeField(blank=True, null=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aprobaciones', to='Tienda.documento')),
                ('vendedor', models.ForeignKey(limit_choices_to={'tipo_usuario': 'VENDEDOR'}, on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
        ),
    ]
