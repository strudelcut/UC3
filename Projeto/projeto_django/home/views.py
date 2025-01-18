from django.shortcuts import render, redirect
from . models import Remetente, Usuario

# Create your views here.

usuarios = Usuario.objects.all()
a = {'title': 'Home - Blog'}
b = {'title': 'Newsletter - Cadastro'}
c = {'title': 'Lista', 'usuarios': usuarios}

def home(request):
    return render(request, 'home/index.html', a)

def newsletter(request):
    return render(request, 'home/newsletter.html', b)

def cadastro(request):
    return render(request, 'home/cadastro.html', {'title': 'Cadastro'})

def lista(request):
    usuarios = Usuario.objects.all()
    c = {
        'title': 'Lista',
        'usuarios': usuarios
    }

    return render(request, 'home/listadb.html', c)

def adicionar(request):
    if request.method == 'POST':
        novo_regsitro = Remetente()
        novo_regsitro.nome = request.POST['nome']
        novo_regsitro.email = request.POST['email']
        novo_regsitro.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, newsletter(request), b)

def add_cadastro(request):
    if request.method == 'POST':
        novo_cadastro = Usuario()
        novo_cadastro.nome = request.POST['nome']
        novo_cadastro.sobrenome = request.POST['sobrenome']
        novo_cadastro.sexo = request.POST['sexo']
        novo_cadastro.cep = request.POST['cep']
        novo_cadastro.rua = request.POST['rua']
        novo_cadastro.numero = request.POST['numero']
        novo_cadastro.complemento = request.POST['complemento']
        novo_cadastro.bairro = request.POST['bairro']
        novo_cadastro.cidade = request.POST['cidade']
        novo_cadastro.uf = request.POST['uf']
        novo_cadastro.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, cadastro(request))