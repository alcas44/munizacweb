from django.contrib import admin
from .models import *

# Register your models here.
class CategoriaEventosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


class EventosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


class RequisitoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")  


class OficinaAdmin(admin.ModelAdmin):
   readonly_fields=("created","updated")            


admin.site.register(CategoriaEvento,CategoriaEventosAdmin)
admin.site.register(Eventos,EventosAdmin)  
admin.site.register(Requisito,RequisitoAdmin)
admin.site.register(Oficina,OficinaAdmin)    