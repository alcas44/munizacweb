from django.core.checks import messages
from django.shortcuts import redirect, render
from LoginApp.forms import FrmLogin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.contrib.sessions.models import Session
# Create your views here.

def login(request):
    formulario = FrmLogin()
    if request.method == "POST":
        formulario = FrmLogin(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                va = User.objects.filter(username=username)
                auth=True              
                return render(request,'TuEspacioApp/index.html',{'va':va,'logeo':auth})
            else:
                auth=False
                return render(request,'LoginApp/error.html',{'msj':'Error de Autenticacion','logeo':auth})  

      
    return render(request,"LoginApp/login.html",{'formulario':formulario})



def salir(request):
    logout(request)
    messages.Info(request,"Sesion Terminada")
    return redirect('/login/')
