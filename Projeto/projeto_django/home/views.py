from django.shortcuts import render, redirect, reverse
from . models import Remetente, Usuario

# Create your views here.

usuarios = Usuario.objects.all()
a = {'title': 'Home - Blog'}
b = {'title': 'Newsletter - Cadastro'}
c = {'title': 'Lista', 'usuarios': usuarios}

def home(request):
    num_visitas = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visitas + 1
    a = {'title': 'Home - Blog', 'num_visitas': num_visitas}
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

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.sobrenome = request.POST['sobrenome']
        usuario.sexo = request.POST['sexo']
        usuario.cep = request.POST['cep']
        
    return render(request, 'home/editar.html', {'edit': usuario})

def editar_cadastro(request, id):
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
    return redirect(reverse('mostrar'))

def apagar(request, id):
    cadastro = Usuario.objects.get(id=id)
    cadastro.delete()
    return redirect(reverse('mostrar'))


def sessao(request):
       
    if request.method == 'POST':
        # Obtém o valor do campo de formulário
        sessao = request.POST.get('usuario')


        # Define a chave na sessão com o valor obtido
        request.session['login'] = sessao


    return render(
        request,
        'home/sessao.html',
    )


def exibir_valor(request):


    # Obtenha o valor da sessão
    # Defina um valor padrão se a sessão estiver vazia
    login = request.session.get('login', 'Nenhum valor definido')  
   
    contexto = {'login': login}
   
    return render(
        request,
        'home/exibir_valor.html',
        contexto,
    )

def encerrar_sessao(request):
    # Use o método clear() para limpar todos os dados da sessão
    request.session.clear()


    return exibir_valor(request)