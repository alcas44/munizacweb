from django.shortcuts import render
from NoticiasApp.models import FotosNoticia, Noticia

# Create your views here.
def noticias(request):
    noticias=Noticia.objects.all()# se almacena todo los productos en la bd

    return render(request,"NoticiasApp/noticias.html",{"noticias":noticias})


def notidetalle(request,noticias_id):
    nom=Noticia.objects.filter(id=noticias_id)
    noticia=Noticia.objects.get(id=noticias_id)
    posts=FotosNoticia.objects.filter(nombre_id=noticia)
    return render(request,"NoticiasApp/notidetalles.html",{'noticias':noticia, 'posts':posts,'titulo':nom})  