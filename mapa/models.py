from django.db import models

# Create your models here.

class Territorio (models.Model):

    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)
    pontuacao = models.IntegerField()
    bonus_max = models.IntegerField()
    data_abertura = models.DateField()
    data_encerramento = models.DateField()
    repeticao = models.BooleanField(default=False)