from django.urls import path
from LoginApp import views
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.login, name="Login"),
    path('salir/',views.salir, name="Salir"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)