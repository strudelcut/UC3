from django.shortcuts import render

# Create your views here.
a = {'title': 'Carrossel - Processadores'}

def carrossel(request):
    return render(request, 'carrossel/index.html', a)