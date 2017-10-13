import datetime
from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm, FormularioForm
from main.models import *
from mapa.models import Territorio
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

def cadastrarFormulario(request, id):
    cadastro = False
    territorio = Territorio.objects.get(pk=id)
    if(request.method=="POST"):
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            resumo = form.cleaned_data['resumo']
            planejamento = form.cleaned_data['planejamento']
            abrangencia = form.cleaned_data['abrangencia']
            resultado = form.cleaned_data['resultado']
            arquivozip = request.FILES['arquivozip']
            conclusao = form.cleaned_data['conclusao']
            user = User.objects.get(pk=request.user.pk)
            capitulo_logado = Capitulo_User.objects.get(user_id=user.id)

            dataRealizacao = form.cleaned_data['dataRealizacao']
            relatorio = Formulario(resumo = resumo, planejamento = planejamento,
                                   abrangencia = abrangencia, resultado = resultado,
                                   data_realizacao=dataRealizacao, data_envio=datetime.date.today(),
                                   territorio=territorio,capitulo=capitulo_logado, conclusao=conclusao,arquivo_zip=arquivozip)
            relatorio.save()
            cadastro = True
    form = FormularioForm()
    context = {"form":form, "cadastro" : cadastro ,"id_territorio" : id, "nome_territorio" : str.upper(territorio.nome)}
    return render(request, 'capitulo/relatorio_form.html', context= context)


def corrigirFormulario(request, id):
    if request.method == "GET":
        formulario = Formulario.objects.get(pk=id)
        print(formulario.observacoes)
        formulario_initial = {
            "resumo": formulario.resultado,
            "planejamento" : formulario.planejamento,
            "abrangencia" : formulario.abrangencia,
            "resultado" : formulario.resultado,
            "conclusao" : formulario.conclusao,
            "dataRealizacao" : formulario.data_realizacao,
            "arquivozip" : formulario.arquivo_zip,
            "status" : formulario.status,
            "observacao" : formulario.observacoes,
            "pontuacaoBonus" : formulario.pontuacao_bonus,
        }
        form = FormularioForm(initial=formulario_initial)
        context = {'form' : form, "id_relatorio":id}
        return render(request, 'capitulo/correcao_relatorio.html', context=context)
    else:
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = Formulario.objects.get(pk=id)
            formulario.pontuacao_bonus = form.cleaned_data['pontuacaoBonus']
            formulario.observacoes = form.cleaned_data['observacao']
            formulario.status = form.cleaned_data['status']
            formulario.save()
            return HttpResponseRedirect('/capitulo/formulario/')
