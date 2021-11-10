from django.urls import path
from SesionApp import views
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('', views.LogView.as_view(), name="Sesion"),
    path('',views.exit,name="exit"),
   # path('login/',views.LogView.as_view(),name="login"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)