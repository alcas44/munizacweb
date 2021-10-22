from django.urls import path
from AccesoApp import views
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('', views.acceso, name="Acceso"),
    path('ver/<int:item_id>/', views.ver, name="ver"),#ver nombre de id en bd
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)