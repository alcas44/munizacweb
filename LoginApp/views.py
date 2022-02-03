from django.db import reset_queries
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_start(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=clave)
            if user is not None:
                login(request,user)
                request.session['member_id'] = user.id	
                return redirect('Principal')
            else:
                messages.info(request,'Credenciales Erroneas')
                return redirect('Login')


    form = AuthenticationForm()
    return render(request,'LoginApp/login.html',{'form':form})



def login_end(request):
    del request.session['member_id']
    logout(request)
    messages.success(request,'Sesion Finalizada con Exito')
    return redirect('/')
