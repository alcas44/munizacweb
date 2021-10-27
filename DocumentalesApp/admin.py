from django.contrib import admin
from .models import Documentales
from embed_video.admin import AdminVideoMixin

# Register your models here.
class DocumentalesAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")             


admin.site.register(Documentales,DocumentalesAdmin)