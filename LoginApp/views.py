from django.shortcuts import redirect, render
from LoginApp.forms import FrmLogin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
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
                #print(va)
                return render(request,'TuEspacioApp/index.html',{'va':va,'logeo':auth})
            else:
                print('No')    



       
    return render(request,"LoginApp/login.html",{'formulario':formulario})