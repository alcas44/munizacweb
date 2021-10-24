from django.shortcuts import redirect, render
from .forms import FormularioSolicitud
from django.core.mail import EmailMessage #para enviar correos

# Create your views here.
def solicitud(request):
    formulario_solicitud= FormularioSolicitud()#instanciar
    if request.method=="POST":
        formulario_solicitud=FormularioSolicitud(data=request.POST)
        if formulario_solicitud.is_valid():
           id=request.POST.get("id")
           nombre=request.POST.get("nombre")
           apellido=request.POST.get("apellido")
           dpi=request.POST.get("dpi")
           email=request.POST.get("email")
           depa=request.POST.get("depa")
           muni=request.POST.get("muni")
           medio=request.POST.get("medio")
           contenido=request.POST.get("contenido")
           #preparar envio de archivos
           enviar=EmailMessage("Nueva Solicitud de Informacion",
            "Usuario {} {} con Correo Electronico {} solicita que por medio {}  lo siguiente \n\n {}".format(nombre,apellido,email,medio,contenido),"",
            ["juanchovargas26@gmail.com"],reply_to=[email])
            #enviar los datos
        try:
            enviar.send()
            return redirect("/solicitudonline/?valido")#importar redirect
        except:
            return redirect("/solicitudonline/?novalido")#importar redirect        
           

           #redireccion despues de el envio de post
        #return redirect("/contacto/?valido")#importar redirect 
    

    return render(request,"SolicitudApp/solicitud.html",{'formulario':formulario_solicitud})

# Create your views here.

# def solicitud(request):
#     return render(request,"SolicitudApp/solicitud.html")