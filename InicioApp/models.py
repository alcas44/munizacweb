from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Oficina(models.Model):
    nombre=models.CharField(max_length=150)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="oficina"
        verbose_name_plural="oficinas"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin   
#-------------------Banner Cabecera------------------------


class CategoriaEvento(models.Model):
    nombre=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="categoriaevento"
        verbose_name_plural="categoriaseventos"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin


class Eventos(models.Model):
    nombre=models.CharField(max_length=75)
    descripcion=models.CharField(max_length=200)
    categoria=models.ForeignKey(CategoriaEvento,on_delete=CASCADE)
    oficina=models.ForeignKey(Oficina,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="eventos",null=True,blank=True)
    fecha=models.DateField()
    hora=models.CharField(max_length=20)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="evento"
        verbose_name_plural="eventos"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin    


 
 #modelo para requisitos

class Requisito(models.Model):
    nombre=models.CharField(max_length=150)
    oficina=models.ForeignKey(Oficina,on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=150)
    documento=models.FileField(upload_to="archivos_requisitos")
    imagen=models.ImageField(upload_to="archivos_requisitos/img")#300x300
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="requisito"
        verbose_name_plural="requisitos"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin       


       