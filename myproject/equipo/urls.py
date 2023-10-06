
from django.urls import path
from django.views.generic import TemplateView 

from . import views

app_name = "equipo"

urlpatterns = [
        path("",TemplateView.as_view(template_name = "equipo/index.html"), name = "index"),
        path("equipocategoria/list/",views.EquipoCategoriaList.as_view(), name = "equipocategoria_list"),
        path("equipocategoria/detail/<int:pk>",views.EquipoCategoriaDetail.as_view(), name = "equipocategoria_detail"),
        path("equipocategoria/create/",views.EquipoCategoriaCreate.as_view(), name = "equipocategoria_create"),
        path("equipocategoria/update/<int:pk>",views.EquipoCategoriaUpdate.as_view(), name = "equipocategoria_update"),
         path("equipocategoria/delete/<int:pk>",views.EquipoCategoriaDelete.as_view(), name = "equipocategoria_delete"),
        
    
    
    
    
    
]



