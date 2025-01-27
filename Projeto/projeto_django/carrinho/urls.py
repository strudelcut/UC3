from django.urls import path
from . import views
    
urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('adicionarv2/<int:produto_id>/', views.adicionar_ao_carrinhoV2, name='adicionar_ao_carrinhov2'),
    path('', views.exibir_carrinho, name='carrinho'),
    path('carrinhov2/', views.exibir_carrinhoV2, name='carrinhov2'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('removerv2/<int:produto_id>/', views.remover_do_carrinhoV2, name='remover_do_carrinhov2'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
]