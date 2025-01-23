from django.shortcuts import render

# Create your views here.

a = {'title': 'Carrossel - Processadores'}

def car(request):
    return render(request, 'car/index.html', a)

