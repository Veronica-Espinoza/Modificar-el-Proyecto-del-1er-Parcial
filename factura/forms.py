from django.forms import ModelForm, EmailInput
from factura.models import Factura

class FacturaFormulario(ModelForm):
    class Meta:
        model = Factura
        fields = ('fecha','proveedores', 'cliente', 'producto', 'cantidad', 'total')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }