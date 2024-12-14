"""
URL configuration for exercicio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from principal import views as views_principal
# from local import views as views_local
# from outros import views as views_outros
# from sobre import views as views_sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', include('principal.urls')),
    path('', include('principal.urls')),
    path('local/', include('local.urls')),
    path('ondeestamos/', include('local.urls')),
    path('outros/', include('outros.urls')),
    path('atividades/', include('outros.urls')),
    path('sobre/', include('sobre.urls')),
    path('produtos/', include('outros.urls')),
    path('servicos/', include('outros.urls')),
]
