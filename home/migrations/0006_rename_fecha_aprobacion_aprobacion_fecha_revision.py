# Generated by Django 4.2.1 on 2023-07-02 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_aprobacion_vendedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aprobacion',
            old_name='fecha_aprobacion',
            new_name='fecha_revision',
        ),
    ]
