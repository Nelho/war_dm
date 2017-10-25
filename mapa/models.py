from django.db import models

# Create your models here.
class Territorio(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)
    pontuacao = models.IntegerField()
    bonus_max = models.IntegerField()
    data_abertura = models.DateField()
    data_encerramento = models.DateField()
    repeticao = models.BooleanField(default=False)
    coord_top = models.CharField(max_length=20)
    coord_left = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="fotos/territorios/")

    class Meta:
        unique_together = (('nome'),)

    def natural_key(self):
        return self.nome

    def __str__(self):
        return self.nome