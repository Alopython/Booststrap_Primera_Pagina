from django import forms


from . import models


class compra_equiposForm(forms.ModelForm):
    
    class Meta:
        model = models.compra_equipos
        fields = ["descripcion", "tipo","fecha_fabricacion","origen_fabriacion","proyecto"]