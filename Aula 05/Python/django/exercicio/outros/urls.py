from django.urls import path
from . import views

urlpatterns = [
    path('', views.outros),
    path('atividades/', views.atividades),
]