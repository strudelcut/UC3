from django.shortcuts import render
from .models import Pessoa

# Create your views here.

# Carregar o objeto, classe Pessoa
pessoas = Pessoa.objects.all()

contexto = {
    'title': 'Cadastro - Salão de Beleza Visual da Moda',
    'pessoas': pessoas
    }

# Carregar o template cadastro.html
def cadastro(request):
    return render(request, 'cadastro/index.html', contexto)

# Salvar os dados de contato
def salvar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    return cadastro(request)

# Mostrar os dados de contato e carregar o template mostrar.html
def mostrar(request):
    pessoas = Pessoa.objects.all()
    contexto = {
    'title': 'Cadastro - Salão de Beleza Visual da Moda',
    'pessoas': pessoas
    }
    return render(request, 'cadastro/mostrar.html', contexto)

# Editar os dados de contato
def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(request, 'cadastro/editar.html', {'pessoa': pessoa})

# Atualizar os dados de contato
def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.idade = request.POST.get('idade')
    pessoa.email = request.POST.get('email')
    pessoa.save()
    return mostrar(request)

# Apagar os dados de contato
def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return mostrar(request)