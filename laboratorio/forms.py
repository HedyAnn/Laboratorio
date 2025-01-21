from django.forms import ModelForm

# Importación de modelos
from .models import Laboratorio, DirectorGeneral, Producto

#=======================================================================================================================================
# Forms 
#=======================================================================================================================================

class Laboratorio_Form(ModelForm):
    class Meta:
        model = Laboratorio
        fields = [
            'nombre',
            'ciudad',
            'pais',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Laboratorio_Form, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class':'form-control'})
        self.fields['pais'].widget.attrs.update({'class':'form-control'})
        
        
class DirectorGeneral_Form(ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = [
            'nombre',
            'laboratorio',
            'especialidad'
        ]
        
    def __init__(self, *args, **kwargs):
        super(DirectorGeneral_Form, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['laboratorio'].widget.attrs.update({'class':'form-control'})
        self.fields['especialidad'].widget.attrs.update({'class':'form-control'})
        
        
class Producto_Form(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'laboratorio',
            'f_fabricacion',
            'p_costo',
            'p_venta',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Producto_Form, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['laboratorio'].widget.attrs.update({'class':'form-control'})
        self.fields['f_fabricacion'].widget.attrs.update({'class':'form-control'})
        self.fields['p_costo'].widget.attrs.update({'class':'form-control'})
        self.fields['p_venta'].widget.attrs.update({'class':'form-control'})