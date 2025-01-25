from django.db import models

# Create your models here.
class Topico(models.Model):
    id   = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30)
    foto = models.ImageField()
    conteudo = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return f'{self.id} - {self.tema} - {self.preco}'