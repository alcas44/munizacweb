from django.forms import models
from django.shortcuts import redirect, render
from SolicitudApp.models import Solicitar
from .forms import FormularioSolicitud
from django.core.mail import EmailMessage #para enviar correos
import random

# Create your views here.
def solicitud(request):
    
    form = FormularioSolicitud()
    if request.method =="POST":
        form = FormularioSolicitud(request.POST)

        if form.is_valid():
          # almacenamiento de datos
          data = Solicitar()
          data.nombre = form.cleaned_data['nombre']
          data.apellido = form.cleaned_data['apellido']
          data.dpi = form.cleaned_data['dpi']
          data.email = form.cleaned_data['email']
          data.depa = form.cleaned_data['depa']
          data.muni = form.cleaned_data['muni']
          data.medio = form.cleaned_data['medio']
          data.contenido = form.cleaned_data['contenido']
          data.token = random.randint(10000,99999)+1
          data.save()
          
          # envio de correo de confirmacion
          email=EmailMessage("Confirmacion para Solicitud de Datos",
            "El Usuario {} {} \n\n con Numero de Solicitud {} \n\n ha solicitado {} \n\n para ser enviado por medio {} al correo {}"
            .format(data.nombre,data.apellido,data.token,data.contenido,data.medio,data.email),"",
            ["cescmazariegos@gmail.com"],["cescmc44@gmail.com"],reply_to=[data.email])
            #enviar los datos
        try:
            email.send()
            return redirect("/solicitudonline/?valido")#importar redirect
        except:
            return redirect("/solicitudonline/?novalido")#importar redirect    

        

    return render(request,"SolicitudApp/solicitud.html",{"formulario":form})

