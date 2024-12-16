from django.shortcuts import render

# Create your views here.
a = {'title': 'Cadastro - Salão de Beleza Visual da Moda'}
def cadastro(request):
    return render(request, 'cadastro/index.html', a)