from django.shortcuts import render, redirect
from carrinho.models import ItemCarrinho
from produto.models import Topico

# Create your views here.
def adicionar_ao_carrinho(request, produto_id):
    produto = Topico.objects.get(id=produto_id)
    item, created = ItemCarrinho.objects.get_or_create(produto=produto)
    if not created:
        item.quantidade += 1
    item.save()
    return redirect('carrinho')

def exibir_carrinho(request):
    itens = ItemCarrinho.objects.all()
    total = 0
    for item in itens:
        item.total_preco = item.produto.preco * item.quantidade
        total += item.total_preco
    return render(request, 'carrinho/index.html', {'itens': itens,'total': total}) 

import urllib.parse  
def finalizar_compra(request):
    itens = ItemCarrinho.objects.all()
    mensagem = "Resumo da Compra:\n"
    for item in itens:
        mensagem += f"{item.produto.tema} (x{item.quantidade}): R$ {item.produto.preco * item.quantidade:.2f}\n"
    mensagem += f"\nTotal: R$ {sum(item.produto.preco * item.quantidade for item in itens):.2f}"

    ItemCarrinho.objects.filter(id__in=[item.id for item in itens]).delete()
    url = f"https://api.whatsapp.com/send?phone=+55219999999&text={urllib.parse.quote(mensagem)}"
    return redirect(url, target="_blank")

def remover_do_carrinho(request, produto_id):
    itens = ItemCarrinho.objects.filter(id=produto_id)
    if itens.exists():
        item = itens.first()
        if item.quantidade > 1:
            item.quantidade -= 1
            item.save()
        else:
            item.delete()
    return redirect('carrinho')