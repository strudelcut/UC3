from django.shortcuts import render
from rest_framework import viewsets
from produto.serializers import TopicoSerializer
from produto.models import Topico

# Create your views here.

def produto(request):
    contexto = {'title' : 'Produto | By Elias'}
    return render(request, 'produto/index.html', contexto)


class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer


def produto(request):
    contexto = {'title' : 'Produto | By Elias', 'produtos': Topico.objects.all()}
    return render(request, 'produto/index.html', contexto)
