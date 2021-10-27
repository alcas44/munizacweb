from django.shortcuts import render
from DocumentalesApp.models import Documentales
# Create your views here.
def documentales(request):
    doc=Documentales.objects.all()
    return render(request,"DocumentalesApp/documentales.html",{"doc":doc})