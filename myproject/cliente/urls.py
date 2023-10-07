
from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
        path('', views.index, name = "index"),
        path("crear/", views.crear, name = "crear"),
        
    
    
    
    
    
]



