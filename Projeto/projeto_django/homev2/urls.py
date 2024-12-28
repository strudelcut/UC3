from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homev2, name='homev2'),
    path('soquetes/', views.soquetes, name='soquetes'),
]