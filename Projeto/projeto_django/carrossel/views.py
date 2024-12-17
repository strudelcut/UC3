from django.shortcuts import render

# Create your views here.
a = {'title': 'Carrossel'}

def carrossel(request):
    return render(request, 'carrossel.html', a)