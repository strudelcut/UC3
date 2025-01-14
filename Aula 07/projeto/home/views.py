from django.shortcuts import render

# Create your views here.

contexto = {'title': 'Home - Salão de Beleza Visual da Moda'}

def home(request):
    # Número de visitas a esta visualização, conforme contado na variável de sessão.
    num_visitas = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visitas + 1


    contexto = {
        'title' : 'Home | By Elias',
        'num_visitas': num_visitas,
    }

    return render(request, 'home/index.html', contexto)

def sessao(request):
       
    if request.method == 'POST':
        # Obtém o valor do campo de formulário
        sessao = request.POST.get('usuario')
        # Define a chave na sessão com o valor obtido
        request.session['login'] = sessao
    return render(request, 'home/sessao.html',)


def exibir_valor(request):
    # Obtenha o valor da sessão
    # Defina um valor padrão se a sessão estiver vazia
    login = request.session.get('login', 'Nenhum valor definido')  
   
    # if 'Adoniran' in login:
    #     contexto = {'login' : 'Administrador'}
    # else:    
    #     contexto = {'login': login}

    if login == 'Adoniran':
        login = 'Administrador'
    
    contexto = {'login': login}
   
    return render(request, 'home/exibir_valor.html', contexto,)


def encerrar_sessao(request):
    # Use o método clear() para limpar todos os dados da sessão
    request.session.clear()
    return exibir_valor(request)