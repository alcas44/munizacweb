from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
from InicioApp.models import Oficina

# Create your models here.
#-------------------Noticias------------------------

class CategoriaNoticia(models.Model):
    nombre=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="categorianoticia"
        verbose_name_plural="categoriasnoticias"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin


class Noticia(models.Model):
    nombre=models.CharField(max_length=75)
    descripcion=models.CharField(max_length=200)
    categoria=models.ForeignKey(CategoriaNoticia,on_delete=CASCADE)
    oficina=models.ForeignKey(Oficina,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="noticias")
    ubicacion=models.CharField(max_length=100,null=True,blank=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="noticia"
        verbose_name_plural="noticias"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin



class FotosNoticia(models.Model):
    nombre=models.ForeignKey(Noticia,on_delete=CASCADE)
    imagen=models.ImageField(upload_to="noticias/fotosnoticia")
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="fotonoticia"
        verbose_name_plural="fotosnoticias"

    def __str__(self):
        return str(self.nombre) #como va a aparecer en el panel admin    
