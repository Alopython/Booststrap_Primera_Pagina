from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#importar LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

from .import models,forms


class EquipoCategoriaList(ListView):
    model = models.EquipoCategoria
    
    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.EquipoCategoria.objects.filter(nombre__icontains = consulta)
        else: 
            object_list = models.EquipoCategoria.objects.all()
        return object_list
            
            
    
class EquipoCategoriaDetail(DetailView):
    model = models.EquipoCategoria
    
class EquipoCategoriaCreate(CreateView,LoginRequiredMixin):
    model = models.EquipoCategoria
    form_class = forms.EquipoCategoriaForm
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
class EquipoCategoriaUpdate(UpdateView,LoginRequiredMixin):
    model = models.EquipoCategoria
    form_class = forms.EquipoCategoriaForm
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
class EquipoCategoriaDelete(DeleteView,LoginRequiredMixin):
    model = models.EquipoCategoria
    success_url = reverse_lazy("equipo:equipocategoria_list")
    
