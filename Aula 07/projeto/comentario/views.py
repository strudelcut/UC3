from django.shortcuts import render
from .models import Comentarios

# Create your views here.

def comentario(request):
    comentarios = Comentarios.objects.all()

    contexto = {
        'title': 'Comentários - Salão de Beleza Visual da Moda',
        'comentarios': comentarios
        }
    return render(request, 'comentario/index.html', contexto)

def gravar(request):
    novo_comentario = Comentarios()
    novo_comentario.nome = request.POST.get('nome')
    novo_comentario.descricao = request.POST.get('descricao')
    novo_comentario.save()
    return comentario(request)

