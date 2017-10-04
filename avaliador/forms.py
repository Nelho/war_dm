from django import forms
from django.contrib.auth.models import User
from main.models import Usuario
from django.forms import ModelForm

REGIONS_CHOICES = (
	("R1", "1º Região"),
	("R2", "2º Região"),
	("R3", "3º Região"),
	("R4", "4º Região"),
	("R5", "5º Região"),
	("R6", "6º Região"),
	("R7", "7º Região"),
	)

class AvaliadorForm(forms.Form):
	
	nome = forms.CharField(label="Nome", max_length=50, widget=forms.TextInput())
	sobrenome = forms.CharField(label="Sobrenome", max_length=50, widget=forms.TextInput(), required=False)
	login = forms.CharField(label="Identidade DeMolay", max_length=50, widget=forms.NumberInput())
	senha = forms.CharField(label="senha", max_length=50, widget=forms.TextInput(), required=False)
	email = forms.CharField(widget=forms.EmailInput())
	telefone = forms.CharField(label="telefone", max_length=20, widget=forms.TextInput(), required=False)
	regiao = forms.ChoiceField(label="região", choices=REGIONS_CHOICES)
	foto = forms.ImageField(label="Foto", required=False)

class AvaliadorEditForm(forms.Form):

	nome = forms.CharField(label="Nome", max_length=50, widget=forms.TextInput())
	sobrenome = forms.CharField(label="Sobrenome", max_length=50, widget=forms.TextInput())
	email = forms.CharField(widget=forms.EmailInput())
	telefone = forms.CharField(label="telefone", max_length=20, widget=forms.TextInput())
	regiao = forms.ChoiceField(label="região", choices=REGIONS_CHOICES)
	foto = forms.ImageField(label="Foto", required=False)

class AvaliadorEditPasswordForm(forms.Form):
	senha_atual = forms.CharField(label="senha atual", max_length=20, widget=forms.PasswordInput())
	nova_senha = forms.CharField(label="nova senha", max_length=20, widget=forms.PasswordInput())
	repetir_senha = forms.CharField(label="repetir nova senha", max_length=20, widget=forms.PasswordInput())