from django import forms
from django.forms.widgets import *

class FrmLogin(forms.Form):
    username = forms.CharField(label='Usuario',required=True ,max_length=100,
               widget=forms.TextInput(attrs={'autofocus': 'autofocus','placeholder':'Usuario'}))

    password = forms.CharField(label='Contraseña',required=True ,max_length=100,
               widget=forms.PasswordInput(attrs={'placeholder':'Password'}))  
