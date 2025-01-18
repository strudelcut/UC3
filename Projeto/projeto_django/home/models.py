from django.db import models

# Create your models here.

class Remetente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    sexo = models.CharField(max_length=1)
    cep = models.TextField(max_length=255)
    rua = models.TextField(max_length=255)
    numero = models.TextField(max_length=255)
    complemento = models.TextField(max_length=255)
    bairro = models.TextField(max_length=255)
    cidade = models.TextField(max_length=255)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.id} - {self.nome} {self.sobrenome}'