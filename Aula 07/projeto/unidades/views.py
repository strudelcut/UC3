from django.shortcuts import render

# Create your views here.
a = {'title': 'Unidades - Salão de Beleza Visual da Moda'}

def unidades(request):
    return render(request, 'unidades/index.html', a)