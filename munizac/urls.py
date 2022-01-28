"""munizac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth.views import LoginView
from django.contrib.auth.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciudad/',include('CiudadApp.urls')),
    path('noticias/',include('NoticiasApp.urls')),
    path('contacto/',include('ContactoApp.urls')),
    path('acceso/',include('AccesoApp.urls')),
    path('leyes/',include('LeyesApp.urls')),
    path('solicitudonline/',include('SolicitudApp.urls')),
    path('documentales/',include('DocumentalesApp.urls')),
    path('login/',include('LoginApp.urls')),
    path('tuespacio/',include('EspacioApp.urls')),
    path('',include('InicioApp.urls')),
]
