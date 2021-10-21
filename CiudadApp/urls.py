from django.urls import path
from CiudadApp import views

urlpatterns = [
    path('', views.ciudad, name="Ciudad"),
]
