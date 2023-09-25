from django import forms


from . import models


class compra_equiposForm(forms.ModelForm):
    
    class Meta:
        model = models.compra_equipos
        fields = ["descripcion", "tipo","fecha","pais_origen"]