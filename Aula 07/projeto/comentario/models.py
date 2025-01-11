from django.db import models

# Create your models here.

class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)