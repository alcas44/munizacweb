from django.contrib import admin
from .models import LeyesDocs

# Register your models here.
class LeyesDocsAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")




admin.site.register(LeyesDocs,LeyesDocsAdmin)