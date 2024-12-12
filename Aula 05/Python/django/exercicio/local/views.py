from django.shortcuts import render

# Create your views here.
def local(request):
    return render(request, 'local/index.html')

def ondeestamos(request):
    return render(request, 'local/ondeestamos.html')