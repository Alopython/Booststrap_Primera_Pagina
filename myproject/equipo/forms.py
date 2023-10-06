
from django import forms
from typing import Any

from . import models


class EquipoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.EquipoCategoria
        fields = "__all__"
        
        
    widgest = {
        
        "nombre": forms.TextInput(attrs={"class": "form-control"}),
        "descripcion": forms.TextInput(attrs={"class":"form-control"}),
        
        
        
    }    
    
        
        
