from django.shortcuts import render
from CiudadApp.models import LugarTop,Recomendado

# Create your views here.
def ciudad(request):
    lugares=LugarTop.objects.all()# se almacena todo los productos en la bd
    recomendados=Recomendado.objects.all()# se almacena todo los productos en la bd

    return render(request,"CiudadApp/ciudad.html",{"lugares":lugares,"recomendados":recomendados})