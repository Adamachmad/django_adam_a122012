from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    ##path('', views.home, name='home'),
    path('profil', views.profil, name='profil'),
    path('contact', views.contact, name='contact')
]