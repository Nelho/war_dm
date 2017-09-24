from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):

	def __str__(self):
		return self.user.username

	class Meta:
		db_table = "usuario" #isso define o nome da tabela no banco

	REGIONS_CHOICES = (
		("R1", "1º Região"),
		("R2", "2º Região"),
		("R3", "3º Região"),
		("R4", "4º Região"),
		("R5", "5º Região"),
		("R6", "6º Região"),
		("R7", "7º Região"),
		)

	CHOICES_TYPE_USERS = (
		("AVA", "Avaliador"),
		("CAP", "Capítulo")
		) 

	user = models.OneToOneField(User)
	regiao = models.CharField(max_length=2, choices=REGIONS_CHOICES, default = "R1")
	tipoUsuario = models.CharField(max_length=3, choices=CHOICES_TYPE_USERS, default= "AVA")

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


class Contato(models.Model):
	class Meta:
		db_table = "contato" #isso define o nome da tabela no banco

	usuario = models.ForeignKey(User, db_column="usuario_id")
	contato = models.CharField(max_length=128)