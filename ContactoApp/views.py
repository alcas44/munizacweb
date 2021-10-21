from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage #para enviar correos

# Create your views here.
def contacto(request):
    formulario_contacto= FormularioContacto()#instanciar
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
           nombre=request.POST.get("nombre")
           email=request.POST.get("email")
           contenido=request.POST.get("contenido")
           #preparar envio de archivos
           email=EmailMessage("Mensaje desde App Django",
            "Usuario {} con la Direccion {} se expresa la princesa \n\n {}".format(nombre,email,contenido),"",
            ["juanchovargas26@gmail.com"],reply_to=[email])
            #enviar los datos
        try:
            email.send()
            return redirect("/contacto/?valido")#importar redirect
        except:
            return redirect("/contacto/?novalido")#importar redirect        
           

           #redireccion despues de el envio de post
        #return redirect("/contacto/?valido")#importar redirect 
    

    return render(request,"ContactoApp/contacto.html",{'formulario':formulario_contacto})
