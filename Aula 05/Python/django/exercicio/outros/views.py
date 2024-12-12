from django.shortcuts import render

# Create your views here.

def outros(request):
    return render(request, 'outros/index.html')

def atividades(request):
    return render(request, 'outros/atividades.html')