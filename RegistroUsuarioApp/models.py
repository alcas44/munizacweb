from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class RegistroUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField()
    usuario = models.ForeignKey(User,on_delete=CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="registrousuario"
        verbose_name_plural="registrosusuarios"

    def __str__(self):
        return self.dpi #como va a aparecer en el panel admin 
