from django.shortcuts import render,redirect
from .models import InfoUsuario

def principal(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:   
        return render(request,'EspacioApp/principal.html')


def perfil(request):
    return render(request,'EspacioApp/perfil.html')


def actividad(request):
    return render(request,'EspacioApp/actividad.html')


def iusi(request):
    return render(request,'EspacioApp/iusi.html')


def agua(request):
    return render(request,'EspacioApp/agua.html')


def desechos(request):
    return render(request,'EspacioApp/desechos.html')


def buzon(request):
    return render(request,'EspacioApp/buzon.html')


def solicitar(request):
    return render(request,'EspacioApp/solicitudes.html')


def tumuni(request):
    info = InfoUsuario.objects.all()
    return render(request,'EspacioApp/tumuni.html',{'info':info}) 


def fullperfil(request):
    return render(request,'EspacioApp/completar.html')