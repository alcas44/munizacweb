from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class LugarTop(models.Model):
    nombre=models.CharField(max_length=150)
    ubicacion=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=350)
    imagen=models.ImageField(upload_to="ciudad")
    punto1=models.CharField(max_length=150)
    punto2=models.CharField(max_length=150,null=True,blank=True)
    punto3=models.CharField(max_length=150,null=True,blank=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="lugartop"
        verbose_name_plural="lugarestops"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin


class Recomendado(models.Model):
    nombre=models.CharField(max_length=150)
    ubicacion=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to="ciudad")
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="recomendado"
        verbose_name_plural="recomendados"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin




