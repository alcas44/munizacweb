from django.urls import path
from ContactoApp import views

urlpatterns = [
    path('', views.contacto, name="Contacto"),
]
