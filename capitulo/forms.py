import datetime
from django import forms

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

    numero = forms.IntegerField(label="telefone" ,widget=forms.TextInput(
        attrs={"maxlength":4, "id": "numero", "class":"w3-input w3-border",
               "type":"number", "placeholder" : "Número do Capítulo", "onkeyup":"funcCriarLogin()"}))

    mestreCosenheiro = forms.CharField(label="mestreConsenheiro", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Mestre consenheiro atual"}))

    regiao = forms .ChoiceField(label="região", choices=REGIONS_CHOICES)
    regiao.widget.attrs["class"] = "w3-white w3-border w3-border-red w3-round-large w3-large"
    regiao.widget.attrs["id"]="regiaoId"
    regiao.widget.attrs["style"] = "width:65%"

    telefone = forms.CharField(label="telefone", widget=forms.TextInput(
        attrs={
		"id":"telefone","class": "w3-input w3-border","placeholder": "Número de whatsapp"}))

    dataFundacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(
        attrs={"type": "date"}))
    dataInstalacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={"type": "date"}))

    foto = forms.ImageField(label='foto', required=False)

class FormularioForm(forms.Form):
    STATUS_CHOICES = (
        ("S1", "Aprovado"),
        ("S2", "Negado"),
        ("S3", "Correção"),
        ("S4", "Enviado"),
    )
    resumo = forms.CharField(label="resumo", widget=forms.Textarea(),required=False)
    planejamento = forms.CharField(label="planejamento", widget=forms.Textarea(),required=False)
    abrangencia = forms.CharField(label="abrangencia", widget=forms.Textarea(),required=False)
    resultado = forms.CharField(label="resultado", widget=forms.Textarea(),required=False)
    dataRealizacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(
        attrs={"type": "date"}),required=False)
    arquivozip = forms.FileField(label="arquivozip", required=False)
    conclusao = forms.CharField(label="conclusao", widget=forms.Textarea(),required=False)
    pontuacaoBonus = forms.IntegerField(label="pontuacaoBonus", required=False)
    observacao = forms.CharField(label="observacao", max_length=256,  widget=forms.Textarea(), required=False)
    status = forms.ChoiceField(label="status",choices=STATUS_CHOICES, required=False)

class CapituloEditForm(forms.Form):
    mestreCosenheiro = forms.CharField(label="mestreConsenheiro", widget=forms.TextInput(
        attrs={"class":"w3-input w3-border", "type":"text", "placeholder" : "Mestre consenheiro atual"}))
    telefone = forms.CharField(label="telefone", widget=forms.TextInput(
        attrs={"id":"telefone","class": "w3-input w3-border","placeholder": "Número de whatsapp"}))
    foto = forms.ImageField(label='foto', required=False)
    email = forms.CharField(label="email", required=False,  widget=forms.TextInput(
        attrs={"id":"emailId","class": "w3-input w3-border","placeholder": "E-mail", "type" : "email"}))

class CapituloEditSenhaForm(forms.Form):
    senhaAtual = forms.CharField(label="senhaAtual", widget=forms.TextInput(attrs={"type":"password"}))
    novaSenha = forms.CharField(label="novaSenha",widget=forms.TextInput(attrs={"type":"password"}))
    confSenha = forms.CharField(label="confSenha",widget=forms.TextInput(attrs={"type":"password"}))