from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gabinete_User(models.Model):

	def __str__(self):
		return self.user.first_name

	class Meta:
		db_table = "gabinete_user" #isso define o nome da tabela no banco

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
		("GR", "MCE"),
        ("GR", "MCEA"),
        ("GR", "Grande Conselho"),
		("AV", "MCR")
		)

	user = models.OneToOneField(User)
	regiao_correcao = models.CharField(max_length=2, choices=REGIONS_CHOICES, default = "R1")
	regiao = models.CharField(max_length=2, choices=REGIONS_CHOICES, default = "R1")
	foto = models.ImageField(upload_to="fotos/")
	tipo_usuario = models.CharField(max_length=2, choices=CHOICES_TYPE_USERS, default= "AV")