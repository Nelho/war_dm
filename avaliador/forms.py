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
	nome = forms.CharField(label="Nome", max_length=50, widget=forms.TextInput(attrs={
		"class": "w3-input",
		"placeholder": "Nome do avaliador"
		}))
	sobrenome = forms.CharField(label="Sobrenome", max_length=50, widget=forms.TextInput(attrs={
		"class": "w3-input",
		"placeholder": "Nome do avaliador"
		}))
	login = forms.CharField(label="Identidade DeMolay", max_length=50, widget=forms.NumberInput(attrs={
		"class": "w3-input",
		"placeholder": "ID avaliador"
		}))
	senha = forms.CharField(label="senha", max_length=50, widget=forms.PasswordInput(attrs={
		"class": "w3-input",
		"placeholder": "Senha avaliador"
		}))
	regiao = forms.ChoiceField(label="região", choices=REGIONS_CHOICES)
	regiao.widget.attrs["class"] = "w3-select w3-border w3-btn w3-red btn-clone w3-hover-red"
	regiao.widget.attrs["name"] = "option"
	email = forms.CharField(widget=forms.EmailInput(attrs={
		"class": "w3-input",
		"placeholder": "E-mail avaliador"
		}))
	telefone = forms.CharField(label="telefone", max_length=20, widget=forms.TextInput(attrs={
		"id":"telefone",
		"class": "w3-input",
		"placeholder": "Número de whatsapp"}))
	foto = forms.ImageField(label="Foto", required=False)
	foto.widget.attrs["id"] = "foto"
	foto.widget.attrs["style"] = "display:none;"
