from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm
from login.models import *


def cadastrarCapitulo(request):
    if(request.method == 'POST'):
        form = CapituloUserForm(request.POST)
        if form.is_valid():
            avaliador = form.cleaned_data['avaliador']
            userCapitulo = form.cleaned_data['usuarioCap']
            dataFundacao = form.cleaned_data['dataFundacao']
            dataInstacao = form.cleaned_data['dataInstalacao']
            mestreConsenheiro = form.cleaned_data['mestreCosenheiro']
            numero = form.cleaned_data['numero']

            capitulo = UsuarioCapitulo(avaliador = avaliador, usuarioCap= userCapitulo, mestreConselheiro= mestreConsenheiro,
                                       dataFundacao= dataFundacao, dataInstalacao= dataInstacao, numero= numero)
            capitulo.save()
        return HttpResponseRedirect('/admin')
    form = CapituloUserForm()
    context_form_set = {"form" : form.as_p()}
    return render(request, 'capitulo/cadastroCapitulo.html', context=context_form_set)