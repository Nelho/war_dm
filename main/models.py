from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
	class Meta:
		db_table = "contato" #isso define o nome da tabela no banco

	usuario = models.ForeignKey(User, db_column="usuario_id")
	contato = models.CharField(max_length=128)