from django.contrib import admin
from .models import *

# Register your models here.
class RegistroUsuarioAdmin(admin.ModelAdmin):
    list_display=['dpi','nombre','apellido']
    list_filter=['dpi']
    readonly_fields=("created","updated")



admin.site.register(RegistroUsuario,RegistroUsuarioAdmin)    

