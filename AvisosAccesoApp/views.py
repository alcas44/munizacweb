from django.shortcuts import render

# Create your views here.
def avisos(request):
    return render(request,"AvisosAccesoApp/avisos.html")