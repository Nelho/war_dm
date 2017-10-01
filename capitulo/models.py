from django.db import models
from main.models import Usuario

# Create your models here.
class UsuarioCapitulo(models.Model):
	def __str__(self):
		return self.usuarioCap.user.username

	class Meta:
		db_table = "usuario_capitulo" #isso define o nome da tabela no banco

	numero = models.IntegerField(primary_key=True)
	dataFundacao = models.DateField()
	dataInstalacao = models.DateField()
	mestreConselheiro = models.CharField(max_length=128)
	avaliador = models.ForeignKey(Usuario, related_name="avaliador_cap", db_column="avaliador_capitulo_id")
	usuarioCap = models.ForeignKey(Usuario, related_name="usuario_cap", db_column="usuario_capitulo_id")