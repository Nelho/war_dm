from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import *
from main.models import *
from django.contrib.auth.decorators import permission_required, login_required
from capitulo.models import *
from main.views import redirect
from avaliador.models import Gabinete_User

@login_required()
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
            user.set_password(senha)
            permission = Permission.objects.get(codename="pode_cadastrar_relatorio")
            user.save()
            user.user_permissions.add(permission)

            telefone = form.cleaned_data['telefone']
            contato = Contato(usuario=user, contato=telefone)
            contato.save()
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

@login_required()
def cadastrarRelatorio(request, id):
    controle = controle_de_acesso(request)
    if controle != True:
        return controle
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
            if not request.user.has_perm('capitulo.pode_cadastrar_relatorio'):
                url_redirect = redirect(request)
                context = {"url": request.build_absolute_uri(), "url_redirect": url_redirect}
                return render(request, "acesso_negado.html", context=context)
            territorios = Territorio.objects.all()
            capitulo = Capitulo_User.objects.get(user=request.user.pk)
            context = {"cadastro": cadastro,"msgSucesso":"Relatório cadastrado com sucesso!", "capitulo": capitulo, "capitulos": buscaCapitulos(), "territorios": territorios}
            return render(request, "capitulo/capitulo_home.html", context=context)

    form = FormularioForm()
    capitulo = Capitulo_User.objects.get(user=request.user.pk)
    context = {"capitulo" : capitulo, "capitulos" : buscaCapitulos() ,"form":form, "cadastro" : cadastro ,"id_territorio" : id, "nome_territorio" : str.upper(territorio.nome)}
    return render(request, 'capitulo/relatorio_form.html', context= context)


def buscaCapitulos():
    capitulos = Capitulo_User.objects.all()
    return capitulos

@login_required()
def home(request):
    controle = controle_de_acesso(request)
    if controle != True:
        return controle
    territorios = Territorio.objects.all()
    capitulo = Capitulo_User.objects.get(user=request.user.pk)
    context = {"capitulo": capitulo ,"capitulos" : buscaCapitulos(), "territorios": territorios}
    return render(request, "capitulo/capitulo_home.html", context=context)

@login_required()
def edit(request):
    controle = controle_de_acesso(request)
    if controle != True:
        return controle
    user = User.objects.get(pk=request.user.pk)
    if(request.method == "GET"):
        capitulo = Capitulo_User.objects.get(user=user.pk)
        try:
            contato = Contato.objects.get(usuario=capitulo.user.pk)
            contato = contato.contato
        except:
            contato = ''
        form_initial = {
            "mestreCosenheiro" : capitulo.mestre_conselheiro,
            "telefone" : contato,
            "email" : user.email,
        }
        capituloEdit = CapituloEditForm(initial= form_initial)
        context = {"form" : capituloEdit, "capitulo" : capitulo,"capitulos" : buscaCapitulos()}
        return render(request, "capitulo/edit_dados_capitulo.html", context=context)
    else:
        form = CapituloEditForm(request.POST, request.FILES)
        if(form.is_valid()):
            usuario = request.user
            capitulo = Capitulo_User.objects.get(user=usuario.pk)
            try:
                contato = Contato.objects.get(usuario=usuario.pk)
                contato.contato = form.cleaned_data['telefone']
            except:
                contato = Contato(contato=form.cleaned_data['telefone'], usuario=capitulo)

            usuario.email = form.cleaned_data['email']
            capitulo.mestre_conselheiro = form.cleaned_data['mestreCosenheiro']

            if(form.cleaned_data['foto'] != None):
                capitulo.foto = form.cleaned_data['foto']

            usuario.save()
            capitulo.save()
            contato.save()

            context = {"cadastro": True,"msgSucesso":"Dados alterados com sucesso!", "capitulo": capitulo, "capitulos": buscaCapitulos()}
            return render(request, "capitulo/capitulo_home.html", context=context)

@login_required()
def alterarSenha(request):
    controle = controle_de_acesso(request)
    if controle != True:
        return controle
    user = User.objects.get(pk=request.user.pk)
    capitulo = Capitulo_User.objects.get(user=user)
    if request.method == "POST":
        form = CapituloEditSenhaForm(request.POST)
        if form.is_valid():
            senha_atual = form.cleaned_data["senhaAtual"]
            nova_senha = form.cleaned_data["novaSenha"]
            conf_senha = form.cleaned_data["confSenha"]

            if nova_senha != conf_senha:
                senhaValida = False
                context = {"form": CapituloEditSenhaForm(),"capitulos" : buscaCapitulos(), "capitulo": capitulo, "error": True, "msgError": "Senhas diferentes!"}
                return render(request, "capitulo/edit_senha_capitulo.html", context=context)
            else:
                if user.check_password(senha_atual):
                    user.set_password(nova_senha)
                    user.save()
                    login(request, user)
                    senhaValida = True
                    context = {"msgSucesso": "Senha alterada com sucesso!", "cadastro":True, "capitulo": capitulo, "capitulos" : buscaCapitulos(), "error": False, "method": "POST"}
                    return render(request, "capitulo/capitulo_home.html", context=context)
                else:
                    senhaValida = False
                    context = {"form": CapituloEditSenhaForm(),"capitulo": capitulo, "capitulos" : buscaCapitulos(),"error": True, "msgError": "Senha atual incorreta!"}
                return render(request, "capitulo/edit_senha_capitulo.html", context=context)
    form = CapituloEditSenhaForm()
    senha_validada = True
    context = {"form": form, "capitulo": capitulo, "capitulos" : buscaCapitulos(), "senha_validada": senha_validada, "method": "GET"}
    return render(request, "capitulo/edit_senha_capitulo.html", context=context)

def regras(request):
    ##if(request.user.pk != None):
    context = {"capitulos": buscaCapitulos()}
    return render(request, "capitulo/regras_capitulo.html", context=context)

def avaliadores(request):
    ##if(request.user.pk != None):
    avaliadoresMCR = Gabinete_User.objects.filter(tipo_usuario='AV')
    context = {"capitulos": buscaCapitulos(), "avaliadores":avaliadoresMCR}
    return render(request, "capitulo/avaliadores_capitulo.html", context=context)

def legenda_territorios(request):
    print(datetime.date.today())
    ##data_encerramento__gte gte significa maior ou igual
    ##data_encerramento__lte lte significa menor ou igual
    ## bigger then
    ## less then
    territorios = Territorio.objects.filter(data_encerramento__gte=datetime.date.today()).order_by("data_encerramento")
    context = {"capitulos": buscaCapitulos(),
                "territorios": territorios,
                "data_atual": datetime.date.today()}
    return render(request, "capitulo/legenda_territorios.html", context=context)

def controle_de_acesso(request):
    if not request.user.has_perm('capitulo.pode_cadastrar_relatorio'):
        url_redirect = redirect(request)
        context = {"url":request.build_absolute_uri(), "url_redirect": url_redirect}
        return render(request, "acesso_negado.html", context=context)
    else:
        return True