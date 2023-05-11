# Generated by Django 4.2 on 2023-05-11 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
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
        migrations.AddField(
            model_name='repuesto',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.vehiculo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.ingreso')),
                ('repuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.repuesto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.factura')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.vehiculo')),
            ],
        ),
    ]