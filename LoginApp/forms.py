from django import forms
from django.db.models import fields
from .models import *

# Create your models here.

class FormLogin(forms.ModelForm):
    user=forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus','placeholder':'Nombre de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:#nombre que tendran en singular y plural
        model = Sesion
        fields = ('user','password')