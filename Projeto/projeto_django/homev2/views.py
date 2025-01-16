from django.shortcuts import render

# Create your views here.
# a = {'title': 'Home V2 - Blog'}
# b = {'title': 'Soquetes'}

def homev2(request):
    return render(request, 'homev2/index.html', {'title': 'Home V2 - Blog'})

def soquetes(request):
    return render(request, 'homev2/soquetes.html', {'title': 'Soquetes'})

def newsletterV2(request):
    return render(request, 'homev2/newsletter.html', {'title': 'Newsletter'})
