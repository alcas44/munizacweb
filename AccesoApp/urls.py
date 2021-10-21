from django.urls import path
from AccesoApp import views

urlpatterns = [
    path('', views.acceso, name="Acceso"),
]
