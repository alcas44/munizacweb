from django.contrib import admin
from .models import *

# Register your models here.
class CategoriaNoticiaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class FotosNoticiaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")             


admin.site.register(CategoriaNoticia,CategoriaNoticiaAdmin)
admin.site.register(Noticia,NoticiaAdmin)  
admin.site.register(FotosNoticia,FotosNoticiaAdmin)