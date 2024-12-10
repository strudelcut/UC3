from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contato(request):
    print('Passei pelo contato')
    return HttpResponse('<body bgcolor="#FFF8DC"><h1>Contato</h1><p>Elias Santos</p><p>Email: elias.santos@rj.senac.br</p></body>')