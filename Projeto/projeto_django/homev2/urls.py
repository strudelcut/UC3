from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homev2, name='homev2'),
    path('soquetes/', views.soquetes, name='soquetes'),
    path('newsletter/', views.newsletterV2, name='newsletterv2'),
    path('cadastro/', views.cadastroV2, name='cadastrov2'),
    path('editar/<int:id>', views.editarV2, name='editarv2'),
    path('mostrar/', views.listaV2, name='mostrarv2'),
    path('salvar/', views.add_cadastroV2, name='salvarv2'),
    path('atualizar/<int:id>', views.editar_cadastroV2, name='atualizarv2'),
    path('apagar/<int:id>', views.apagarV2, name='apagarv2'),
]