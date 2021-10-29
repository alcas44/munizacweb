from django.shortcuts import render
from .forms import FormLogin

# Create your views here.

def login(request):
    formulario_login = FormLogin()
    if request.method == "POST":
        formulario_login = (FormLogin.request.POST)
    return render(request,"LoginApp/login.html",{"form":formulario_login})