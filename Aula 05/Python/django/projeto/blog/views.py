from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    # print('Passei pelo blog')
    # return HttpResponse('<body bgcolor="yellow"><h1>Alô Mundo!</h1></body>')
    return render(request, 'blog/index.html')

def artigo(request):
    return render(request, 'blog/artigo.html')
