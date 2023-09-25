from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Proyecto)
admin.site.register(models.compra_equipos)
admin.site.register(models.venta_equipos)