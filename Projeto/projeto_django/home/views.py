from django.shortcuts import render

# Create your views here.
a = {'title': 'Home - Blog'}

def home(request):
    return render(request, 'global/base.html', a)
