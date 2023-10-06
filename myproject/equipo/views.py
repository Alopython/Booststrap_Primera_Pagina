from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.

from .import models,forms


class EquipoCategoriaList(ListView):
    model = models.EquipoCategoria
    
class EquipoCategoriaDetail(DetailView):
    model = models.EquipoCategoria
    
class EquipoCategoriaCreate(CreateView):
    model = models.EquipoCategoria
    form_class = forms.EquipoCategoriaForm
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
class EquipoCategoriaUpdate(UpdateView):
    model = models.EquipoCategoria
    form_class = forms.EquipoCategoriaForm
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
class EquipoCategoriaDelete(DeleteView):
    model = models.EquipoCategoria
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
