from email.policy import default
from django.db import models

# Create your models here.

class Planta(models.Model):
    nome = models.CharField(max_length = 64)
    descricao = models.TextField(default = "")
    imagem = models.ImageField(default = "")
    dificuldade = models.CharField(max_length = 16, default = "")
    quantidade_agua = models.FloatField(default = 0.0)
    quantidade_fertilizante = models.FloatField(default = 0.0)
    tipo_fertilizante = models.CharField(max_length = 64, default = "")

    def __str__(self):
        return f"{self.nome}"


class Utilizador(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"


class PlantaCuidada(models.Model):
    planta = models.ForeignKey(Planta, on_delete = models.CASCADE)
    utilizador = models.ForeignKey(Utilizador, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.planta} do {self.utilizador}"
    

class Tratamento(models.Model):
    planta_cuidada = models.ForeignKey(PlantaCuidada, on_delete = models.CASCADE)
    instante = models.DateTimeField(auto_now=True)
    quantidade_agua = models.FloatField(default = 0.0)
    quantidade_fertilizante = models.FloatField(default = 0.0)

    def __str__(self):
        return f"{self.planta_cuidada} : {self.quantidade_agua} litros de água e {self.quantidade_fertilizante} kg de fertilizante na data: {self.instante}"


class Monitorizacao(models.Model):
    planta_cuidada = models.ForeignKey(PlantaCuidada, on_delete = models.CASCADE)
    instante = models.DateTimeField(auto_now=True)
    luz = models.FloatField(default = 0.0)
    humidade = models.FloatField(default = 0.0)
    temperatura = models.FloatField(default = 0.0)
    condutividade = models.FloatField(default = 0.0)

    def __str__(self):
        return f"{self.planta_cuidada} em {self.instante} tem {self.luz} de luz, {self.humidade} de humidade, {self.temperatura} de temperatura e {self.condutividade} de condutividade"

    
class Notificacao(models.Model):
    planta_associada = models.ForeignKey(Planta, on_delete = models.CASCADE)
    descricao = models.TextField(default = "")
    criticidade = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.planta_associada} tem nível critico {self.criticidade}"