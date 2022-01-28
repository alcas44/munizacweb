from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_start,name="Login"),
    path('logout/',views.login_end,name="Logout"),
]
