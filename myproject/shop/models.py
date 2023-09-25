from django.db import models

# Create your models here.



class EquipoFijo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) ->str:
        return self.nombre
    
class EquipoRotativo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) ->str:
        return self.nombre
