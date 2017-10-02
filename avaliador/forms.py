from django import forms

class AvaliadorForm(forms.Form):
	REGIONS_CHOICES = (
		("R1", "1º Região"),
		("R2", "2º Região"),
		("R3", "3º Região"),
		("R4", "4º Região"),
		("R5", "5º Região"),
		("R6", "6º Região"),
		("R7", "7º Região"),
		)
	nome = forms.CharField(label="Nome", max_length=50, widget=forms.TextInput())
	login = forms.CharField(label="Identidade DeMolay", max_length=50, widget=forms.NumberInput())
	senha = forms.CharField(label="senha", max_length=50, widget=forms.PasswordInput())
	confirmar_senha = forms.CharField(label="confirmar_senha", max_length=50, widget=forms.PasswordInput())
	email = forms.CharField(widget=forms.EmailInput())
	telefone = forms.CharField(label="telefone", max_length=20, widget=forms.TextInput())
	regiao = forms.ChoiceField(label="região", choices=REGIONS_CHOICES)
	foto = forms.ImageField(label="Foto", required=False)
