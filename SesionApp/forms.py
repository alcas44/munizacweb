from django import forms
from django.forms import models
from django.forms.widgets import Textarea

class FrmSesion(forms.Form):
    username = forms.CharField(label='Usuario',required=True ,max_length=100,
    widget=forms.TextInput(attrs={'placeholder':'Usuario','autofocus':'autofocus'}))
    password = forms.CharField(label='Password',required=True,max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    
