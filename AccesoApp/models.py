from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Item(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to="items/img")#300x300
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="item"
        verbose_name_plural="items"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin 


#guardado de dato en los items
# Nombre de los Folders Contenedores

class FolderItem(models.Model):
    nombre=models.CharField(max_length=30)
    agno=models.CharField(max_length=4)#sin guiones ni comas
    
