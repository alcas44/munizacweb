from django import forms
from django.forms.widgets import Textarea

class FormularioSolicitud(forms.Form):
    nombre = forms.CharField(label='Nombre',required=True ,max_length=100)
    apellido=forms.CharField(label='Apellido',required=True,max_length=100)
    dpi=forms.CharField(label='DPI(No Guiones)',required=True,max_length=13)#no guiones
    email =forms.EmailField(label='Correo Electronico',required=True ,max_length=100)
    depa=forms.CharField(label='Departamento',required=True,max_length=100)
    muni=forms.CharField(label='Municipio',required=True,max_length=100)
    medio=forms.CharField(label='Medio Envio de los Solicitado',required=True,max_length=100)
    contenido=forms.CharField(label='Contenido Solicitado' ,max_length=400,widget=forms.Textarea)
    