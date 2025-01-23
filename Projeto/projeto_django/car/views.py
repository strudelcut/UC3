from django.shortcuts import render
from rest_framework import viewsets
from home.serializers import SerializarImagem
from home.models import Imagem

# Create your views here.

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = SerializarImagem

a = {'title': 'Carrossel - Processadores'}

def car(request):
    
    a = {'title': 'Carrossel - Processadores', 'imagens' : Imagem.objects.all()}
    return render(request, 'car/index.html', a)

