from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request, 'home/index.html')