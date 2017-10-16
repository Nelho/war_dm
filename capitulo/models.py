
from django.db import models
from django.contrib.auth.models import User
from mapa.models import Territorio


# Create your models here.
class Capitulo_User(models.Model):
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "capitulo_user"  # isso define o nome da tabela no banco
        permissions = (
            ('pode_cadastrar_relatorio', 'Pode cadastrar relatório'),
        )

    REGIONS_CHOICES = (
        ("R1", "1º Região"),
        ("R2", "2º Região"),
        ("R3", "3º Região"),
        ("R4", "4º Região"),
        ("R5", "5º Região"),
        ("R6", "6º Região"),
        ("R7", "7º Região"),
    )

    numero = models.IntegerField(primary_key=True)
    data_fundacao = models.DateField()
    data_instalacao = models.DateField()
    mestre_conselheiro = models.CharField(max_length=128)
    regiao = models.CharField(max_length=2 ,choices=REGIONS_CHOICES, default="R1")
    foto = models.ImageField(upload_to="fotos/", null=True)
    user = models.OneToOneField(User)

class Formulario(models.Model):

    class Meta:
        db_table = "formulario"  # isso define o nome da tabela no banco

    STATUS_CHOICES = (
        ("S1", "Aprovado"),
        ("S2", "Negado"),
        ("S3", "Correção"),
        ("S4", "Enviado"),
    )
    resumo = models.CharField(max_length=500)
    planejamento = models.CharField(max_length=500)
    abrangencia = models.CharField(max_length=500)
    resultado = models.CharField(max_length=500)
    data_realizacao = models.DateField()
    data_envio = models.DateField()
    conclusao = models.CharField(max_length=500)
    arquivo_zip = models.FileField(upload_to='arquivozip/')
    territorio = models.ForeignKey(Territorio, related_name="territorio", db_column="territorio")
    capitulo = models.ForeignKey(Capitulo_User,related_name="capitulo_user", db_column="usuario_capitulo")
    observacoes = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default = "S4")
    pontuacao_bonus = models.IntegerField(null=True)

