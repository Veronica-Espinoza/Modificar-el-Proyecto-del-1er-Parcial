"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from factura.views import agregar_factura, ver_factura, editar_factura, eliminar_factura,generar_reporte
from webapp.views import ver_facturas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ver_facturas, name='inicio'),
    path('agregar_factura/', agregar_factura),
    path('ver_factura/<int:idFactura>', ver_factura),
    path('editar_factura/<int:idFactura>', editar_factura),
    path('eliminar_factura/<int:idFactura>', eliminar_factura),
    path('generar_reporte/', generar_reporte)
]