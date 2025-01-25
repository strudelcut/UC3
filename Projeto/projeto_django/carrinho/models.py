from django.db import models
from home.models import Imagem

# Create your models here.

class ItemCarrinho(models.Model):
    id = models.AutoField(primary_key=True)
    # Chave estrangeira para o produto
    produto = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    # O argumento on_delete=models.CASCADE  serve para que, caso o produto seja deletado,
    # todos os itens do carrinho que contenham este produto também sejam deletados. Isso
    # é util pois um produto  pode ser deletado se ele não est  mais sendo usado em
    # nenhum carrinho.
    
    # Quantidade do produto no carrinho
    quantidade = models.PositiveIntegerField(default=1)
    # Data em que o produto foi adicionado ao carrinho
    adicionado_em = models.DateTimeField(auto_now_add=True)