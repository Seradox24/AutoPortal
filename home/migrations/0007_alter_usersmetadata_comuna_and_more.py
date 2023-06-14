# Generated by Django 4.2.1 on 2023-06-13 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_usersmetadata_comuna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmetadata',
            name='comuna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.comuna'),
        ),
        migrations.AlterField(
            model_name='usersmetadata',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.estado'),
        ),
        migrations.AlterField(
            model_name='usersmetadata',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.genero'),
        ),
        migrations.AlterField(
            model_name='usersmetadata',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.pais'),
        ),
        migrations.AlterField(
            model_name='usersmetadata',
            name='perfiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.perfiles'),
        ),
        migrations.AlterField(
            model_name='usersmetadata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]