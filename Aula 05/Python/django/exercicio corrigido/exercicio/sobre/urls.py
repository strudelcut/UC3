from django.urls import path

from . import views

urlpatterns = [
    path('', views.sobre),
    path('produtos/', views.produtos),
    path('servicos/', views.servicos),
]