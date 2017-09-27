import datetime
from django import forms
from login.models import Usuario, UsuarioCapitulo

class CapituloUserForm(forms.Form):
    REGIONS_CHOICES = (
        ("R1", "1º Região"),
        ("R2", "2º Região"),
        ("R3", "3º Região"),
        ("R4", "4º Região"),
        ("R5", "5º Região"),
        ("R6", "6º Região"),
        ("R7", "7º Região"),
    )
    username = forms.CharField(label="username", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Usuario"}))

    password = forms.CharField(label="password", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"password", "placeholder" : "Senha"}))

    mestreCosenheiro = forms.CharField(label="mestreConsenheiro", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Mestre consenheiro atual"}))

    ##regiao = forms.ChoiceField(label="região", choices=(REGIONS_CHOICES), widget=forms.ChoiceField(
      ##  setattr({"id=":"Demo", "class":"w3-dropdown-content w3-bar-block w3-animate-zoom"})))

    numero = forms.IntegerField(label="numero", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"number", "placeholder" : "Número do Capítulo"}))

    dataFundacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(
        attrs={"type": "date"}))
    dataInstalacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={"type": "date"}))

    avaliador = forms.ModelChoiceField(queryset = Usuario.objects.filter(tipoUsuario="AVA"))


