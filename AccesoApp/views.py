from django.shortcuts import render
from AccesoApp.models import *

# Create your views here.
def acceso(request):
   items=Item.objects.all()# se depliegan todas la data en la bd

   return render(request,"AccesoApp/acceso.html",{"items":items})


def ver(request,item_id):
   nom=Item.objects.filter(id=item_id)
   folder=FolderItem.objects.filter(item_id=item_id)#obtengo el folder
   #data=DocumentosItem.objects.filter(folder_id=folder) 
   return render(request,"AccesoApp/ver.html",{"folder":folder,"titulo":nom})
    