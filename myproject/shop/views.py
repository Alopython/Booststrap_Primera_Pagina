from django.shortcuts import render
from django.shortcuts import redirect



from . import models
from . import forms

# Create your views here.


def index(request):
    proyectos =models.compra_equipos.objects.all()
    return render(request,"shop/index.html",{"proyectos":proyectos})

def crear(request):   
    if request.method == "POST":
        form = forms.compra_equiposForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("shop:index")
    else:
        form = forms.compra_equiposForm()
    return render(request, "shop/crear.html",{"form": form})