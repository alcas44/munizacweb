from django.urls import path
from SolicitudApp import views
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('', views.solicitud, name="Solicitud"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)