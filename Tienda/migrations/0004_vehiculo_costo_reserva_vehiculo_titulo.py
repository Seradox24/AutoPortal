# Generated by Django 4.2 on 2023-05-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_sucursal_remove_vehiculo_costo_reserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='costo_reserva',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
