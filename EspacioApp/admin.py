from django.contrib import admin
from .models import *

class PanelUsuario(admin.ModelAdmin):
   readonly_fields=("created","updated")            


admin.site.register(InfoUsuario,PanelUsuario)
