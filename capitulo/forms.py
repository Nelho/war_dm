import datetime
from django import forms
from login.models import Usuario, UsuarioCapitulo

class CapituloUserForm(forms.Form):
    class Meta:
        model = UsuarioCapitulo

    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=24)
    numero = forms.IntegerField()
    dataFundacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={"type": "date"}))
    dataInstalacao = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={"type": "date"}))
    mestreCosenheiro = forms.CharField(max_length=60)
    avaliador = forms.ModelChoiceField(queryset = Usuario.objects.filter(tipoUsuario="AVA"))
    usuarioCap = forms.ModelChoiceField(queryset = Usuario.objects.filter(tipoUsuario="CAP"))


