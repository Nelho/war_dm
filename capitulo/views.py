from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm, FormularioForm
from main.models import *
from capitulo.models import UsuarioCapitulo


def cadastrarCapitulo(request):
    if(request.method == 'POST'):
        form = CapituloUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            nomeCap = form.cleaned_data['nomeCap']
            password = form.cleaned_data['password']
            numero = form.cleaned_data['numero']
            user = User(username='Cap_'+str(numero), first_name=nomeCap , password=password,
                        email='capitulo_'+str(numero)+'@demolaypb.com.br')
            user.save()

            regiao = form.cleaned_data['regiao']
            usuario = Usuario(user=user, regiao=regiao, tipoUsuario='CAP')
            usuario.save()

            telefone = form.cleaned_data['telefone']
            Contato(usuario=user, contato=telefone)

            avaliador = form.cleaned_data['avaliador']
            dataFundacao = form.cleaned_data['dataFundacao']
            dataInstacao = form.cleaned_data['dataInstalacao']
            mestreConsenheiro = form.cleaned_data['mestreCosenheiro']
            usuarioCap = UsuarioCapitulo(numero=numero, dataFundacao=dataFundacao, dataInstalacao=dataInstacao,
                                         mestreConselheiro=mestreConsenheiro, avaliador=avaliador, usuarioCap=usuario)
            usuarioCap.save()
        return HttpResponseRedirect('/capitulo/cadastro/')
    form = CapituloUserForm()
    context = {"form" : form}
    return render(request, 'capitulo/cadastroCapitulo.html', context=context)

def cadastrarFormulario(request):
    form = FormularioForm()
    context = {"form":form}
    return render(request, 'capitulo/relatorio_form.html', context= context)