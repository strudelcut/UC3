from django.shortcuts import render, redirect, reverse
from rest_framework import viewsets
from home.serializers import SerializarImagem
from home.models import Usuario, Imagem

# Create your views here.
# a = {'title': 'Home V2 - Blog'}
# b = {'title': 'Soquetes'}

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = SerializarImagem
    
def homev2(request):
    return render(request, 'homev2/index.html', {'title': 'Home V2 - Blog'})

def soquetes(request):
    a = {'title': 'Soquetes - Processadores', 'imagens' : Imagem.objects.all()}
    return render(request, 'homev2/soquetes.html', a)

def newsletterV2(request):
    return render(request, 'homev2/newsletter.html', {'title': 'Newsletter'})

def cadastroV2(request):
    return render(request, 'homev2/cadastro.html', {'title': 'Cadastro'})

def editarV2(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.sobrenome = request.POST['sobrenome']
        usuario.sexo = request.POST['sexo']
        usuario.cep = request.POST['cep']
        
    return render(request, 'homev2/editar.html', {'edit': usuario})

def listaV2(request):
    usuarios = Usuario.objects.all()
    c = {
        'title': 'Lista',
        'usuarios': usuarios
    }

    return render(request, 'homev2/listadb.html', c)

def add_cadastroV2(request):
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
    return render(request, cadastroV2(request))

def editar_cadastroV2(request, id):
    novo_cadastro = Usuario.objects.get(id=id)
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
    return redirect(reverse('mostrarv2'))

def apagarV2(request, id):
    cadastro = Usuario.objects.get(id=id)
    cadastro.delete()
    return redirect(reverse('mostrarv2'))