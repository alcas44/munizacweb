from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class LeyesDocs(models.Model):
    nombre = models.CharField(max_length=100)
    documento=models.FileField(upload_to="items/documentos/leyes")
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="ley"
        verbose_name_plural="leyes"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin 