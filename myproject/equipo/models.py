from django.db import models
from django.utils import timezone

# Create your models here.

class EquipoCategoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, null=True, verbose_name="descripcion")
    
    class Meta:
        verbose_name = "categoria de equipos"
        verbose_name_plural = "categorias de equipos"
    
    def __str__(self) -> str:
        return self.nombre
    
    
class Equipo(models.Model):
    """Equipos que corresponde  a una categoria"""
    categoria = models.ForeignKey(EquipoCategoria, on_delete=models.SET_NULL,blank=True,null=True,verbose_name="categoria")
    nombre = models.CharField(max_length=100)
    unidad_de_medida= models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, null=True, verbose_name="descripcion")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False,verbose_name="fecha de actualizacion")
    
    class Meta:
        verbose_name = "equipos"
        verbose_name_plural = "equipos"
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio}"
    
    
    