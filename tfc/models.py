from email.policy import default
from django.db import models

# Create your models here.

class Condicao(models.Model):
    dificuldade = models.CharField(max_length=16)
    expo_solar = models.IntegerField(default=0)
    quantidade_agua = models.IntegerField(default=0)
    quantidade_fertilizante = models.IntegerField(default=0)

    def __str__(self):
        return self.dificuldade
    

class Planta(models.Model):
    nome = models.CharField(max_length = 64)
    descricao = models.CharField(max_length = 512)
    imagem = models.ImageField(default = "")
    condicoes = models.ManyToManyField(Condicao)

    def __str__(self):
        return self.nome


class Utilizador(models.Model):
    nome = models.CharField(max_length=64)
    genero = models.CharField(max_length=16)
    idade = models.IntegerField(default=0)
    plantas = models.ManyToManyField(Planta)

    def __str__(self):
        return self.nome

