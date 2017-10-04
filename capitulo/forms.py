import datetime
from django import forms
from main.models import Usuario
from capitulo.models import UsuarioCapitulo


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
    nomeCap = forms.CharField(label="username", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Nome do capítulo"}))

    password = forms.CharField(label="password", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"password", "placeholder" : "Senha"}))

    passwordConfirm = forms.CharField(label="password", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"password", "placeholder" : "Confimar senha"}))

    mestreCosenheiro = forms.CharField(label="mestreConsenheiro", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Mestre consenheiro atual"}))

    regiao = forms .ChoiceField(label="região", choices=REGIONS_CHOICES)
    regiao.widget.attrs["class"] = "w3-white w3-border w3-border-red w3-round-large w3-large"
    regiao.widget.attrs["id"]="regiaoId"
    regiao.widget.attrs["style"] = "width:65%"

    numero = forms.IntegerField(label="telefone" ,widget=forms.TextInput(
        attrs={"maxlength": "4", "id": "numero", "class":"w3-input w3-border",
               "type":"number", "placeholder" : "Número do Capítulo", "onkeyup":"funcCriarLogin()"}))

    email = forms.CharField(label="emailCap", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "E-mail"}))

    telefone = forms.IntegerField(label="telefone", widget=forms.TextInput(
        attrs={
		"id":"telefone","class": "w3-input w3-border","placeholder": "Número de whatsapp"}))

    dataFundacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(
        attrs={"type": "date"}))
    dataInstalacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={"type": "date"}))

    #avaliador = forms.ModelChoiceField(queryset = Usuario.objects.filter(tipoUsuario="AVA"))
    #avaliador.widget.attrs["class"] = "w3-select w3-btn w3-ripple w3-red"
    #avaliador.widget.attrs["id"]="regiaoId"
    #avaliador.widget.attrs["style"] = "width:15%"

class FormularioForm(forms.Form):
    resumo = forms.CharField(label="resumo", widget=forms.Textarea())
    planejamento = forms.CharField(label="planejamento", widget=forms.Textarea())
    abrangencia = forms.CharField(label="abrangencia", widget=forms.Textarea())
    resultado = forms.CharField(label="resultado", widget=forms.Textarea())
    dataRealizacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(
        attrs={"type": "date"}))
    arquivozip = forms.FileField(label="arquivozip", required=False)
    conclusao = forms.CharField(label="conclusao", widget=forms.Textarea())