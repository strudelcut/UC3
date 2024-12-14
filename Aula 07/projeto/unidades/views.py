from django.shortcuts import render

# Create your views here.
def unidades(request):
    return render(request, 'unidades/index.html')