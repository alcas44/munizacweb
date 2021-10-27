from django.shortcuts import render

# Create your views here.
def leyes(request):
    return render(request,"LeyesApp/leyes.html")