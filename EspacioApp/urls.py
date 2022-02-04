from unicodedata import name
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 
from . import views

urlpatterns = [
    path('',views.principal,name="Principal"),
    path('miperfil/',views.perfil,name="Perfil"),
    path('miactividad/',views.actividad,name="Actividad"),
    path('iusi/',views.iusi,name="Iusi"),
    path('deptoagua/',views.agua,name="Agua"),
    path('desechossolidos/',views.desechos,name="Desechos"),
    path('mibuzon/',views.buzon,name="Buzon"),
    path('misolicitud/',views.solicitar,name="Solicitar"),
    path('tumuni/',views.tumuni,name="TuMuni"),
    path('miperfil/completar/',views.fullperfil,name="FullPerfil"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)