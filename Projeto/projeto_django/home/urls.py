from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('add/', views.adicionar, name='novo_registro'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('salvar/', views.add_cadastro, name='salvar'),
    path('mostrar/', views.lista, name='mostrar'),
]