from email.policy import default
from django.db import models

# Create your models here.

class Planta(models.Model):
    nome = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 512)
    imagem = models.ImageField(default = "")

    def __str__(self):
        return self.nome
