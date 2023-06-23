from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from factura.models import Factura
# Create your views here.
def ver_facturas(request):
    cantidad_facturas = Factura.objects.count()
    pagina = loader.get_template('factura.html')
    lista_factura =  Factura.objects.all()
    datos = {'cantidad':cantidad_facturas, 'facturas':lista_factura}
    return HttpResponse(pagina.render(datos, request))