import os
from os import remove
import shutil
from pathlib import Path
from datetime import datetime, date, timedelta
from django.conf import settings
from home.models import *

#RUTA=settings.RUTA
#RUTA2=settings.RUTA2
RUTA= "C:/Users/matia/OneDrive/Documentos/web/Tienda/"
RUTA2="C:/Users/matia/OneDrive/Documentos/web/Tienda/AutoPortal/"


def moverArchivoProducto(file, id):
    if existeArchivoMedia(file)==True:
        fecha = datetime.now()
        nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
        shutil.move(f'{RUTA}AutoPortal/media/{file}', f'{RUTA2}assets/upload/producto/{nombre}')
        Producto.objects.filter(pk=id).update(foto=nombre)

 


def moverArchivoProducto2(file):
    shutil.move(f'{RUTA}AutoPortal/media/producto/{file}', f'{RUTA2}assets/upload/producto/{file}')


 
def moverArchivoProductoGaleria(file, id):
    if existeArchivoMedia(file)==True:
        fecha = datetime.now()
        nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
        shutil.move(f'{RUTA}AutoPortal/media/{file}', f'{RUTA2}assets/upload/producto/{nombre}')
        ProductoFotos.objects.filter(pk=id).update(foto=nombre)

def existeArchivo(carpeta, archivo):
    try:
        ruta=f"{RUTA}AutoPortal/assets/upload/{carpeta}/{archivo}"
        fileObj = Path(ruta)
        return fileObj.is_file()
    except Exception as e:
        return False


def existeArchivoMedia(archivo):
    try:
        ruta=f"{RUTA}AutoPortal/media/{archivo}"
        fileObj = Path(ruta)
        return fileObj.is_file()
    except Exception as e:
        return False
    