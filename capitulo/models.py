
from django.db import models
from main.models import Usuario


# Create your models here.
class UsuarioCapitulo(models.Model):
    def __str__(self):
        return self.usuarioCap.user.username

    class Meta:
        db_table = "usuario_capitulo"  # isso define o nome da tabela no banco

    numero = models.IntegerField(primary_key=True)
    dataFundacao = models.DateField()
    dataInstalacao = models.DateField()
    mestreConselheiro = models.CharField(max_length=128)
    avaliador = models.ForeignKey(Usuario, related_name="avaliador_cap", db_column="avaliador_capitulo_id")
    usuarioCap = models.ForeignKey(Usuario, related_name="usuario_cap", db_column="usuario_capitulo_id")

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
    dataRealizacao = models.DateField()
    dataEnvio = models.DateField()
    arquivoZip = models.FileField(upload_to="documentos/")
    territorio = models.CharField(max_length=30)
    ##capituloUser = models.ForeignKey(Usuario,related_name="usuario_cap", db_column="usuario_capitulo_id")
    observacoes = models.CharField(max_length=500)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default = "S4")
    pontuacaoBonus = models.IntegerField()

