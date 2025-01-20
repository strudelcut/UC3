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
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.editar_cadastro, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('sessao/', views.sessao,name='sessao'),
    path('exibir_valor/', views.exibir_valor, name='exibir_valor'),
    path('encerrar/', views.encerrar_sessao, name='encerrar'),
]