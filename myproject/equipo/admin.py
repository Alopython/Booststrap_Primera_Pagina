from django.contrib import admin
from.import models


admin.site.site_title = "Equipos"
admin.site.site_header = "R&M Ingenieria"


@admin.register(models.EquipoCategoria)
class EquipoCategoriaAdmin(admin.ModelAdmin):
    
    
    list_display = ("nombre" , "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre", )
    
    
    
    
    
@admin.register(models.Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        
     "nombre",
     "unidad_de_medida",
     "cantidad",
     "precio",
     "descripcion",
     "fecha_actualizacion", 
         
        
    )
    
    list_display_links = ("nombre",)
    list_display = ("nombre" , )
    search_fields = ("nombre",)
    ordering = (
        
        "categoria",
        "nombre",
    )
    
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"
    
    
        
        

    
    


# Register your models here.
