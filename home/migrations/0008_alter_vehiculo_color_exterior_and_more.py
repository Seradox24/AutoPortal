# Generated by Django 4.2.1 on 2023-06-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_usersmetadata_comuna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='color_exterior',
            field=models.CharField(choices=[('ROJO', 'Rojo'), ('AZUL', 'Azul'), ('BLANCO', 'Blanco'), ('NEGRO', 'Negro'), ('PLATEADO', 'Plateado')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='condicion',
            field=models.CharField(blank=True, choices=[('NUEVO', 'Nuevo'), ('USADO', 'Usado')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='puertas',
            field=models.IntegerField(choices=[(2, '2 puertas'), (4, '4 puertas'), (5, '5 puertas')]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_vehiculo',
            field=models.CharField(choices=[('SEDAN', 'Sedán'), ('SUV', 'SUV'), ('CAMIONETA', 'Camioneta'), ('HATCHBACK', 'Hatchback'), ('COUPE', 'Coupé')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='ubicacion',
            field=models.CharField(choices=[('IQUIQUE', 'Iquique'), ('ALTO HOSPICIO', 'Alto Hospicio'), ('OTRO', 'Otro')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='volumen_motor',
            field=models.CharField(choices=[('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5')], max_length=20),
        ),
    ]