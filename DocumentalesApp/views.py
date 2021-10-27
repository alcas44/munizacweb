from django.shortcuts import render

# Create your views here.
def documentales(request):
    return render(request,"DocumentalesApp/documentales.html")