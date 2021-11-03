from django.shortcuts import render

# Create your views here.
def tuespacio(request):
    return render(request,"TuEspacioApp/index.html")