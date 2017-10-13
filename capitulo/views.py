import datetime
from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm, FormularioForm
from main.models import *
from avaliador.models import Gabinete_User
from capitulo.models import *


def cadastrarCapitulo(request):

    if(request.method == 'POST'):
        form = CapituloUserForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            nomeCap = form.cleaned_data['nomeCap']
            numero = form.cleaned_data['numero']
            login = 'cap_'+str(numero)
            senha = 'cap_'+str(numero)
            print(login)
            print(senha)
            user = User(username=login, first_name=nomeCap , password=senha,
                        email='capitulo_'+str(numero)+'@demolaypb.com.br')
            user.save()

            telefone = form.cleaned_data['telefone']
            Contato(usuario=user, contato=telefone)
            try:
                foto = request.FILES['foto']
            except:
                foto = None
            regiao = form.cleaned_data['regiao']
            dataFundacao = form.cleaned_data['dataFundacao']
            dataInstacao = form.cleaned_data['dataInstalacao']
            mestreConsenheiro = form.cleaned_data['mestreCosenheiro']
            capitulo_user = Capitulo_User(numero=numero,data_fundacao=dataFundacao,data_instalacao=dataInstacao,
                                          mestre_conselheiro=mestreConsenheiro, regiao=regiao, foto=foto, user=user)
            capitulo_user.save()
        return HttpResponseRedirect('/capitulo/cadastro/')
    form = CapituloUserForm()
    context = {"form" : form}
    return render(request, 'capitulo/cadastroCapitulo.html', context=context)

def cadastrarFormulario(request):
    ##print(datetime.date.da)
    if(request.method=="POST"):
        form = FormularioForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            resumo = form.cleaned_data['resumo']
            planejamento = form.cleaned_data['planejamento']
            abrangencia = form.cleaned_data['abrangencia']
            resultado = form.cleaned_data['resultado']
            arquivozip = request.FILES['arquivozip']
            conclusao = form.cleaned_data['conclusao']
            ##usuarioLogado = Usuario.objects.filter(user=request.user.pk)[0]
            user = User.objects.get(pk=request.user.pk)
            capitulo_logado = Capitulo_User.objects.get(user_id=user.id)

            dataRealizacao = form.cleaned_data['dataRealizacao']
            relatorio = Formulario(resumo = resumo, planejamento = planejamento,
                                   abrangencia = abrangencia, resultado = resultado,
                                   dataRealizacao = dataRealizacao, dataEnvio=datetime.date.today(),
                                   territorio="Brasil",capitulo=capitulo_logado, conclusao=conclusao,arquivozip=arquivozip)
            relatorio.save()

    form = FormularioForm()
    context = {"form":form}
    return render(request, 'capitulo/relatorio_form.html', context= context)