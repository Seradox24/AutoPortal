from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from home.models import *
from acceso.decorators import logueado
from utilidades import utilidades, webpay
import json
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import locale

apikeycr=settings.EMAIL_SECRET



import requests
apicmf=settings.CMF_SECRET


# Create your views here.

def send_email(html_content, subject, to_email):
    message = Mail(
        from_email=settings.EMAIL_SENDER,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(apikeycr)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(str(e))
        return None



@logueado()
def carro_inicio(request):
    cuantos=Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).count()
    datos=Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).order_by('-id').all()
    suma=0
    for dato in datos:
        valor=dato.cantidad*dato.producto.precio
        suma=suma+valor
        
    return render(request, 'carro/home.html', {'datos': datos, 'suma': suma, 'cuantos': cuantos,})


@logueado()
def carro_crear(request):
    if request.method =='POST':
        try:
            datos=Producto.objects.filter(pk=request.POST['id']).get()
        except Producto.DoesNotExist:
            raise Http404
        Carrito.objects.create(cantidad=request.POST['cantidad'], producto_id=request.POST['id'], users_metadata_id=request.session['users_metadata_id'])
        return HttpResponseRedirect("/carro")
    else:
        raise Http404


@logueado()
def carro_vaciar(request):
    Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).delete()
    OrdenDeCompra.objects.filter(users_metadata_id=request.session['users_metadata_id']).filter(estado_id=3).delete()
    
    messages.add_message(request, messages.SUCCESS, f'Se vació tu carrito exitosamente!!!.')
    return HttpResponseRedirect('/carro')


@logueado()
def carro_quitar(request, id):
    try:
        datos=Producto.objects.filter(pk=id).get()
    except Producto.DoesNotExist:
        raise Http404
    Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).filter(producto_id=id).delete()
    messages.add_message(request, messages.SUCCESS, f'Se quitó el producto del carrito exitosamente!!!.')
    return HttpResponseRedirect('/carro')


@logueado()
def carro_modificar_cantidad(request, id, cantidad):
    try:
        datos=Carrito.objects.filter(pk=id).get()
    except Carrito.DoesNotExist:
        raise Http404
    Carrito.objects.filter(id=id).update(cantidad=cantidad)
    messages.add_message(request, messages.SUCCESS, f'Se modificó la cantidad del producto {datos.producto.nombre} exitosamente!!!.')
    return HttpResponseRedirect('/carro')


import decimal

@logueado()
def carro_pagar(request):
    api_key = apicmf
    url = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar'
    params = {
        'apikey': api_key,
        'formato': 'json'
    }
    response = requests.get(url, params=params)
    datadl = response.json()
    valor_dolar = datadl['Dolares'][0]['Valor']
    decimal_separator = locale.localeconv()['decimal_point']
    valor_dolar_float = decimal.Decimal(valor_dolar.replace(',', decimal_separator))

    cuantos = Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).count()
    if cuantos == 0:
        return HttpResponseRedirect('/carro')
    datos = Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).order_by('-id').all()

    suma = 0
    for dato in datos:
        valor = dato.cantidad * dato.producto.precio
        suma += valor

    valor_dolar_float = suma / valor_dolar_float
    valor_dolar_formatted = '{:,.2f}'.format(valor_dolar_float)

    usuario = UsersMetadata.objects.filter(id=request.session['users_metadata_id']).get()
    comunas = Comuna.objects.all()
    return render(request, 'carro/pagar.html', {'datos': datos, 'suma': suma, 'usuario': usuario, 'comunas': comunas, 'cuantos': cuantos, 'total_dolar': valor_dolar_formatted,'valor_dolar_float':valor_dolar_formatted,'valor_dolar':valor_dolar})




@logueado()
def carro_webpay(request):
    if request.method =='POST':
        cuantos=Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).count()
        if cuantos==0:
            return HttpResponseRedirect('/carro')
        direccion=f"{request.POST['direccion']} {request.POST['indicaciones']}"
        result=webpay.crearTransaccion(request.session['users_metadata_id'], direccion, request.POST['comuna'])
        return render(request, 'carro/webpay.html', {'url': result['url'], 'token': result['token']})

@logueado()
def carro_webpay_respuesta(request):
    if not request.GET.get('token_ws'):
        raise Http404
    token = request.GET.get('token_ws')
    result = webpay.verificarTransaccion(token)
    
    if result[0] == 'vacio':
        raise Http404
    elif result[0] == 'AUTHORIZED':
        try:
            orden = OrdenDeCompra.objects.filter(users_metadata_id=request.session['users_metadata_id'], estado_id=3).get()
        except OrdenDeCompra.DoesNotExist:
            raise Http404
        
        OrdenDeCompra.objects.filter(users_metadata_id=request.session['users_metadata_id'], estado_transbank=0).update(
            token_ws=token, estado_transbank=result[0], fecha_transbank=result[2], tarjeta=result[1], estado_id=6
        )
        
        suma = 0
        datos = Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).all()
        detalle = ""
        
        for dato in datos:
            valor = dato.cantidad * dato.producto.precio
            suma += valor
            detalle += f"""
            <tr>
                <td style="border: 1px solid black;">
                    <img src="{settings.BASE_URL}assets/upload/producto/{dato.producto.foto}" width="100" height="100">
                </td>
                <td style="border: 1px solid black;">{dato.producto.nombre}s</td>
                <td style="border: 1px solid black;">{dato.cantidad}</td>
                <td style="border: 1px solid black;">${utilidades.numberFormat(dato.producto.precio)}</td>
            </tr>
            """
            OrdenDeCompraDetalle.objects.create(orden_de_compra_id=orden.id, producto_id=dato.producto_id, cantidad=dato.cantidad)
        
        Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).delete()
        usuario = UsersMetadata.objects.filter(id=request.session['users_metadata_id']).get()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <title>el título de la página</title>
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <h1>Hola {usuario}, tu pedido ha sido ingresado al sistema con el N°{orden.id}</h1>
                    <table style="border-collapse: collapse;">
                        <thead>
                            <tr>
                                <th>*</th>
                                <th>Producto</th>
                                <th>Cantidad</th>
                                <th>Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            {detalle}
                            <tr>
                                <td colspan="5" style="border: 1px solid black;">
                                    Total de tu compra
                                </td>
                            </tr>
                            <tr>
                                <td colspan="5" style="border: 1px solid black;">
                                    ${utilidades.numberFormat(suma)}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
        </html>
        """
        
        send_email(html, 'Tienda', usuario.correo)
        send_email(html, 'Tienda', 'ma.inayao@duocuc.cl')
        messages.add_message(request, messages.SUCCESS, f'La orden de compra N° {orden.id} ha sido generada exitosamente. Tu número de transacción de Transbank es {token}. Nos pondremos en contacto contigo a la brevedad para coordinar el envío de los productos. Gracias por tu compra!!!')
        return HttpResponseRedirect('/carro')
    
    elif result[0] == 'FAILED':
        OrdenDeCompra.objects.filter(users_metadata_id=request.session['users_metadata_id']).filter(estado_transbank=0).update(
            token_ws=token, fecha_transbank=result[2], tarjeta=result[1], estado_id=5
        )
        messages.add_message(request, messages.WARNING, f'No fue posible procesar el pago, por favor inténtalo nuevamente!!!.')
        return HttpResponseRedirect('/carro')