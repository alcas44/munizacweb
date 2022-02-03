from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal,name="Principal"),
    path('miperfil/',views.perfil,name="Perfil"),
    path('miactividad/',views.actividad,name="Actividad"),
]
