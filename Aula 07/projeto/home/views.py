from django.shortcuts import render

# Create your views here.

contexto = {'title': 'Home - Salão de Beleza Visual da Moda'}

def home(request):
    return render(request, 'home/index.html', contexto)