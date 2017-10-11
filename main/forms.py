from django import forms
from avaliador.models import Gabinete_User

class LoginForm(forms.Form):
	login = forms.CharField(label="login", max_length=50, 
		widget=forms.TextInput(attrs={
			"class":"form-control", 
			"placeholder": "Digite aqui seu login",
			"id":"usuario"}))
	senha = forms.CharField(label='senha', max_length=50, 
		widget=forms.PasswordInput(attrs={
			"class":"form-control", 
			"placeholder": "Digite aqui sua senha",
			"id":"senha"}))
