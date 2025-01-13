from django.shortcuts import render

# Create your views here.
a = {'title': 'Tabela - Soquetes'}

def tabela(request):
    return render(request, 'tabela/index.html', a)
