from django.db import models

# Create your models here.

class Solicitar(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dpi=models.CharField(max_length=13)
    email=models.EmailField()
    depa=models.CharField(max_length=100)
    muni=models.CharField(max_length=100)
    medio=models.CharField(max_length=100)
    contenido=models.CharField(max_length=500)
    token=models.CharField(max_length=800)