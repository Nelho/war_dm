import datetime

from django.contrib.auth.models import Permission
from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm, FormularioForm
from main.models import *
from django.contrib.auth.decorators import permission_required, login_required
from capitulo.models import *
from main.views import redirect

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

@login_required()
def cadastrarRelatorio(request, id):
    if not request.user.has_perm('capitulo.pode_cadastrar_relatorio'):
        url_redirect = redirect(request)
        context = {"url":request.build_absolute_uri(), "url_redirect": url_redirect}
        return render(request, "acesso_negado.html", context=context)
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
            context = {"cadastro": cadastro,"capitulo": capitulo, "capitulos": buscaCapitulos(), "territorios": territorios}
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
    if not request.user.has_perm('capitulo.pode_cadastrar_relatorio'):
        url_redirect = redirect(request)
        context = {"url":request.build_absolute_uri(), "url_redirect": url_redirect}
        return render(request, "acesso_negado.html", context=context)
    territorios = Territorio.objects.all()
    capitulo = Capitulo_User.objects.get(user=request.user.pk)
    context = {"capitulo": capitulo ,"capitulos" : buscaCapitulos(), "territorios": territorios}
    return render(request, "capitulo/capitulo_home.html", context=context)