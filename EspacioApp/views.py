from django.shortcuts import render,redirect

def principal(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:   
        return render(request,'EspacioApp/principal.html')


#ver si ademas de preguntar si esta autenticado preguntar si tambien esta activado el usuario
#y mandar mensaje a la raiz y decir que no esta autenticado y activo