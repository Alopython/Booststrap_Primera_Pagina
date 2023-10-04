from django.shortcuts import render
from django.views.generic import ListView



# Create your views here.

from .import models


class EquipoCategoriaList(ListView):
    model = models.EquipoCategoria
