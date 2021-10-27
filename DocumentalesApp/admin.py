from django.contrib import admin
from .models import Documentales

# Register your models here.
class DocumentalesAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")             


admin.site.register(Documentales,DocumentalesAdmin)