from django.urls import path
from NoticiasApp import views
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen

urlpatterns = [
    path('', views.noticias, name="Noticias"),
    path('notidetalle/<int:noticias_id>/', views.notidetalle, name="notidetalle"),#ver nombre de id en bd
]
