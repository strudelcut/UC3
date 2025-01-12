from django.shortcuts import render
from . models import Remetente

# Create your views here.

a = {'title': 'Home - Blog'}

def home(request):
    return render(request, 'home/index.html', a)

def newsletter(request):
    return render(request, 'home/newsletter.html', a)

def adicionar(request):
    novo_regsitro = Remetente()
    novo_regsitro.nome = request.POST['nome']
    novo_regsitro.email = request.POST['email']
    novo_regsitro.save()
    return home(request)
