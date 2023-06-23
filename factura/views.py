from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from factura.models import Factura
from factura.forms import FacturaFormulario

# Create your views here.
def agregar_factura(request):
    pagina = loader.get_template('agregar_factura.html')
    if request.method == 'GET':
        formulario= FacturaFormulario
    elif request.method == 'POST':
        formulario= FacturaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_factura(request, idFactura):
    pagina= loader.get_template('ver_factura.html')
    #persona= Persona.objects.get(pk=idPersona)
    factura= get_object_or_404(Factura, pk=idFactura)
    mensaje= {'factura': factura}
    return HttpResponse(pagina.render(mensaje, request))

def editar_factura(request, idFactura):
    pagina= loader.get_template('editar_factura.html')
    #persona= Persona.objects.get(pk=idPersona)
    factura= get_object_or_404(Factura, pk=idFactura)
    if request.method == 'GET':
        formulario= FacturaFormulario(instance=factura)
    elif request.method == 'POST':
        formulario= FacturaFormulario(request.POST, instance=factura)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje= {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))

def eliminar_factura(request, idFactura):
    factura= get_object_or_404(Factura, pk=idFactura)
    if factura:
        factura.delete()
        return redirect('inicio')