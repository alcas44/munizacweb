from django.shortcuts import render
from LeyesApp.models import LeyesDocs
# Create your views here.
def leyes(request):
    docs=LeyesDocs.objects.all()# se depliegan todas la data en la bd
    return render(request,"LeyesApp/leyes.html",{"docs":docs})