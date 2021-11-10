from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from django.views import View
from .forms import FrmSesion
from django.contrib.auth.models import User #Importar modelo de usuario (registrarse)
from django.contrib.auth import login , logout #Guardar Estado
from django.contrib.auth import authenticate  # Autenticación django proporciona tabla de usuarios

#iniciar sesión

class LogView(View):
    def get(self,request):
       frm = FrmSesion()
       return render(request,'SesionApp/login.html',{'frm':frm})

    def post(self, request):
        username = request.POST.get("username")
        # request.session["username"] = username
        # request.session.set_expiry(7 * 24 * 3600)
        password = request.POST.get("password")
        # Consultar si el usuario existe en la tabla de usuarios
        user = authenticate(username=username,password=password)
        if user:
            login(request,user) #Estado de guardado de inicio de sesión directo
            next_url = request.GET.get("next")
            if next_url:
                print(next_url)
                return redirect(next_url) #Sin permiso, vuelve a la página anterior
            return render(request,"TuEspacioApp/index.html") # Ningún parámetro muestra el éxito del inicio de sesión
        else:
            return render(request,"SesionApp/login.html")



def exit(request):
    logout(request)
    return redirect(reverse("/"))

