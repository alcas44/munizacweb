from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sesion(models.Model):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


class Registro(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dpi=models.CharField(max_length=13)
    fecha_nac=models.DateField()
    telefono=models.CharField(max_length=9)
    direccion=models.CharField(max_length=300)
    residencia=models.CharField(max_length=300)
    correo=models.EmailField()
    documento=models.FileField(upload_to="registros/usuarios/pdf")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)  


    class Meta:#nombre que tendran en singular y plural
        verbose_name="registro"
        verbose_name_plural="registros"

    def __str__(self):
        return self.dpi #como va a aparecer en el panel admin   