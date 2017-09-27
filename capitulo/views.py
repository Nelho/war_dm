from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm
from login.models import *


def cadastrarCapitulo(request):
    if(request.method == 'POST'):
        form = CapituloUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(username=username, password=password)
            user.save()

            regiao = form.cleaned_data['regiao']
            usuario = Usuario(user=user, regiao=regiao, tipoUsuario='CAP')
            usuario.save()

            avaliador = form.cleaned_data['avaliador']
            dataFundacao = form.cleaned_data['dataFundacao']
            dataInstacao = form.cleaned_data['dataInstalacao']
            mestreConsenheiro = form.cleaned_data['mestreCosenheiro']
            numero = form.cleaned_data['numero']
            usuarioCap = UsuarioCapitulo(numero=numero, dataFundacao=dataFundacao, dataInstalacao=dataInstacao,
                                         mestreConselheiro=mestreConsenheiro, avaliador=avaliador, usuarioCap=usuario)
            usuarioCap.save()
        return HttpResponseRedirect('/admin')
    form = CapituloUserForm()
    context = {"form" : form}
    return render(request, 'capitulo/cadastroCapitulo.html', context=context)