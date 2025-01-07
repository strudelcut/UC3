from django.shortcuts import render
from .models import Pessoa

# Create your views here.
contexto = {'title': 'Cadastro - Salão de Beleza Visual da Moda'}
def cadastro(request):
    return render(request, 'cadastro/index.html', contexto)

def gravar(request):
    # Salvar os dados de contato
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    return cadastro(request)