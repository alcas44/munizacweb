from django import forms
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre',required=True ,max_length=100)
    email = forms.CharField(label='Correo Electronico',required=True ,max_length=100)
    contenido = forms.CharField(label='Contenido' ,max_length=100,widget=forms.Textarea)
    