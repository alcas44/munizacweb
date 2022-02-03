from django.shortcuts import render,redirect

def principal(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:   
        return render(request,'EspacioApp/principal.html')


def perfil(request):
    return render(request,'EspacioApp/perfil.html')


def actividad(request):
    return render(request,'EspacioApp/actividad.html')
