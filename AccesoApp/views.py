from django.shortcuts import render
from AccesoApp.models import *

# Create your views here.
def acceso(request):
   items=Item.objects.all()# se depliegan todas la data en la bd

   return render(request,"AccesoApp/acceso.html",{"items":items})