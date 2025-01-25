from django.urls import path
from . import views
    
urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('', views.exibir_carrinho, name='carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
]