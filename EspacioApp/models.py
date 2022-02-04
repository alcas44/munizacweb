from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
from InicioApp.models import Oficina
 
class InfoUsuario(models.Model):
    nombre=models.CharField(max_length=300)
    descripcion=models.CharField(max_length=200)
    oficina=models.ForeignKey(Oficina,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="panelusuario",null=True,blank=True)
    fecha=models.DateField()
    hora=models.CharField(max_length=20)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="infousuario"
        verbose_name_plural="infousuarios"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin   




