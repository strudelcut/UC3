from django.shortcuts import render

# Create your views here.
a = {'title': 'Tabela'}

def tabela(request):
    return render(request, 'tabela/index.html', a)
