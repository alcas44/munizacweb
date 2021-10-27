from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from NoticiasApp.models import Oficina

# Create your models here.
class Documentales(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    ubicacion=models.CharField(max_length=100)
    url=models.CharField(max_length=120)
    oficina=models.ForeignKey(Oficina,on_delete=models.CASCADE)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:#nombre que tendran en singular y plural
        verbose_name="documental"
        verbose_name_plural="documentales"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin
