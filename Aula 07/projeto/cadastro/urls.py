from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('salvar/', views.salvar, name='salvar'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]