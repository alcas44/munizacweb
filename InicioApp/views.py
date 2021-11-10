from django.shortcuts import render
from InicioApp.models import Eventos,Requisito

# Create your views here.
def inicio(request):
    eventos=Eventos.objects.all()# se almacena todo los productos en la bd
    requisitos=Requisito.objects.all()# se almacena todo los productos en la bd

    return render(request,"InicioApp/inicio.html",{"eventos":eventos,"requisitos":requisitos})


    