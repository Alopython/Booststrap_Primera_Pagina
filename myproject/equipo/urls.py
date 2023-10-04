
from django.urls import path
from django.views.generic import TemplateView 

from . import views

app_name = "equipo"

urlpatterns = [
        path("",TemplateView.as_view(template_name = "equipo/index.html"), name = "index"),
        path("equipocategoria/list/",views.EquipoCategoriaList.as_view(), name = "equipocategoria_list")
        
    
    
    
    
    
]



