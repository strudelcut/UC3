from django.shortcuts import render, redirect
from . models import Remetente

# Create your views here.

a = {'title': 'Home - Blog'}
b = {'title': 'Newsletter - Cadastro'}

def home(request):
    return render(request, 'home/index.html', a)

def newsletter(request):
    return render(request, 'home/newsletter.html', b)

def adicionar(request):
    if request.method == 'POST':
        novo_regsitro = Remetente()
        novo_regsitro.nome = request.POST['nome']
        novo_regsitro.email = request.POST['email']
        novo_regsitro.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'home/newsletter.html', b)
