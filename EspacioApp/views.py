from django.shortcuts import render,redirect

def principal(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:   
        return render(request,'EspacioApp/principal.html')
