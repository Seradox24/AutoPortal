# Generated by Django 4.2.1 on 2023-07-02 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_aprobacion_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprobacion',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usersmetadata'),
        ),
    ]