from django.shortcuts import render
from avaliador.forms import AvaliadorForm, AvaliadorEditForm, AvaliadorEditPasswordForm
from capitulo.forms import FormularioForm
from django.contrib.auth.models import User, Permission
from avaliador.models import Gabinete_User
from capitulo.models import Capitulo_User, Formulario
from main.models import Contato
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, login_required
from main.views import redirect
from mapa.models import Territorio
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from mapa.views import conquista_capitulo, mapa_geral

# Create your views here.
def cadastro_avaliador(request):
    cadastro = False
    if request.method == "POST":
        form = AvaliadorForm(request.POST, request.FILES)
        if form.is_valid():            
            form_regiao = form.cleaned_data["regiao"]
            form_regiao_correcao = form.cleaned_data["regiao_correcao"]
            if(form_regiao == 'default' or form_regiao_correcao == 'default'):
                context = {"form": form, "cadastro": cadastro, "regiao_error": True}
                return render(request, "avaliador/cadastro_avaliador.html", context=context)

            form_nome = form.cleaned_data["nome"]
            form_sobrenome = form.cleaned_data["sobrenome"]
            form_login = form.cleaned_data["login"]
            form_senha = form_login + "_" + form_nome
            form_email = form.cleaned_data["email"]
            form_telefone = form.cleaned_data["telefone"]
            TIPO_USUARIO = "AV"

            try:
                form_foto = request.FILES["foto"]
            except MultiValueDictKeyError:
                form_foto = ""

            permission = Permission.objects.get(codename='pode_avaliar_capitulo')
            new_user = User.objects.create_user(form_login, password=form_senha,
                                        first_name=form_nome, last_name=form_sobrenome, email=form_email)
            new_user.user_permissions.add(permission)
            new_user.save()
            new_usuario = Gabinete_User(user=new_user,
                                regiao=form_regiao,
                                regiao_correcao=form_regiao_correcao,
                                foto=form_foto,
                                tipo_usuario=TIPO_USUARIO)
            new_usuario.save()
            if len(form_telefone) != 0:
                new_contato = Contato(usuario=new_user, contato=form_telefone)
                new_contato.save()
            cadastro = True

    form = AvaliadorForm()
    context = {"form": form, "cadastro": cadastro }
    return render(request, "avaliador/cadastro_avaliador.html", context=context)

@login_required()
def profile_edit(request):
    controle = controle_acesso(request)
    if controle != True:
        return controle
    if request.method == "POST":
        form = AvaliadorEditForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            usuario = Gabinete_User.objects.get(user_id=request.user.id)

            form_nome = form.cleaned_data["nome"]
            form_sobrenome = form.cleaned_data["sobrenome"]
            form_email = form.cleaned_data["email"]
            form_regiao = form.cleaned_data["regiao"]
            form_telefone = form.cleaned_data["telefone"]
            try:
                form_foto = request.FILES["foto"]
            except MultiValueDictKeyError:
                form_foto = usuario.foto

            try:
                contato = Contato.objects.get(usuario_id=request.user.id)
                contato.contato = form_telefone
                contato.save()
            except Contato.DoesNotExist:
                contato = Contato(usuario=user, contato=form_telefone)
                contato.save()

            user.first_name = form_nome
            user.last_name = form_sobrenome
            user.email = form_email

            usuario.foto = form_foto
            usuario.regiao = form_regiao

            user.save()
            usuario.save()
            return HttpResponseRedirect('/avaliador/home')
    elif request.method == "GET":
        usuario = Gabinete_User.objects.get(user_id=request.user.id)
        capitulos_corrigir = conf_home(request, usuario)
        try:
            telefone = Contato.objects.get(usuario_id=request.user.id)
        except Contato.DoesNotExist:
            telefone = Contato()
            print("usuário sem telefone")
        form_initial = {"nome": request.user.first_name,
                        "sobrenome": request.user.last_name,
                        "email": request.user.email, 
                        "regiao": usuario.regiao,
                        "telefone": telefone.contato}

        form = AvaliadorEditForm(initial=form_initial)
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    context = {"form": form, "capitulos":capitulos_corrigir, "corretor": corretor}
    return render(request, "avaliador/avaliador_edit_profile.html", context=context)

@login_required()
def password_edit(request):
    controle = controle_acesso(request)
    if controle != True:
        return controle
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    capitulos_corrigir = conf_home(request, corretor)
    if request.method == "POST":
        form = AvaliadorEditPasswordForm(request.POST)
        if form.is_valid():
            form_senha_atual = form.cleaned_data["senha_atual"]
            form_nova_senha = form.cleaned_data["nova_senha"]
            form_repetir_senha = form.cleaned_data["repetir_senha"]

            if form_nova_senha != form_repetir_senha:
                senha_validada = False
                # msg_error = "Senhas diferentes!"
                context = {"form": form, "error": True, "msg_error": "Senhas diferentes!", "capitulos":capitulos_corrigir, "corretor": corretor}
                return render(request, "avaliador/avaliador_edit_password.html", context=context)
            else:
                user = User.objects.get(pk=request.user.id)

                if user.check_password(form_senha_atual):
                    user.set_password(form_nova_senha)
                    user.save()
                    login(request, user)
                    senha_validada = True
                    context = {"form": form, "senha_validada": senha_validada, "method": "POST", "capitulos":capitulos_corrigir, "corretor": corretor}
                    return render(request, "avaliador/avaliador_edit_password.html", context=context)
                else:
                    senha_validada = False
                    context = {"form": form, "error": True, "msg_error": "Senha atual incorreta!", "capitulos":capitulos_corrigir, "corretor": corretor}

                return render(request, "avaliador/avaliador_edit_password.html", context=context)
    form = AvaliadorEditPasswordForm()
    senha_validada = True
    context = {"form": form, "senha_validada": senha_validada, "method": "GET", "capitulos":capitulos_corrigir, "corretor": corretor}

    return render(request, "avaliador/avaliador_edit_password.html", context=context)

# função criada para reutilização de código. Ela busca os capítulos e
# quantos relatórios ele possui
############################################
def conf_home(request, corretor, status='S4'):
    capitulos = Capitulo_User.objects.all()
    capitulos_corrigir = []
    for capitulo in capitulos:
        if capitulo.regiao == corretor.regiao_correcao:
            aux = [capitulo, Formulario.objects.filter(capitulo=capitulo.numero, status=status).count()]
            capitulos_corrigir.append(aux)
        else:
            aux = [capitulo, 0]
            capitulos_corrigir.append(aux)
    return capitulos_corrigir

def controle_acesso(request):
    if not request.user.has_perm('avaliador.pode_avaliar_capitulo'):
        url_redirect = redirect(request)
        context = {"url":request.build_absolute_uri(), "url_redirect": url_redirect}
        return render(request, "acesso_negado.html", context=context)
    return True

QTD_ELEMENTOS_POR_PAGINA = 2
def paginator_conf(request, paginator):
    #caso o valor passado como parâmetro no GET seja diferente de número
    try:
        pagina = int(request.GET.get('pagina', '1'))
        pagina = 1 if pagina <= 0 else pagina
    except ValueError:
        pagina = 1

    #caso o número de página passado como parâmetro não esteja dentro do interavalo da consulta no BD
    try:
        relatorios = paginator.page(pagina)
    except (EmptyPage, InvalidPage):
        relatorios = paginator.page(paginator.num_pages)
    return relatorios

filtros_dict = {
    "aprovado": "S1",
    "rejeitado": "S2",
    "correcao": "S3",
    "enviado": "S4"

}
############################################
@login_required()
def avaliador_home(request):
    controle = controle_acesso(request)
    if controle != True:
        return controle

    filtro = request.GET.get("filtro", "enviado")
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    capitulos_corrigir = conf_home(request, corretor)
    relatorios_corrigir = Formulario.objects.filter(capitulo__regiao=corretor.regiao_correcao, 
        status=filtros_dict[filtro]).only('capitulo').order_by('data_envio') # '-data_envio'
    paginator = Paginator(relatorios_corrigir, QTD_ELEMENTOS_POR_PAGINA)    
    relatorios_paginados = paginator_conf(request, paginator)

    context = {"capitulos":capitulos_corrigir, "relatorios": relatorios_paginados, 
    "corretor": corretor, 
    "next": request.path,
    "filtro": filtro}
    return render(request, "avaliador/avaliador_home.html", context=context)

@login_required()
def avaliar_cap(request, numero_cap):
    controle = controle_acesso(request)
    if controle != True:
        return controle

    filtro = request.GET.get("filtro", "enviado")
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    capitulo = Capitulo_User.objects.get(numero=numero_cap)
    capitulos_corrigir = conf_home(request, corretor)
    relatorios_corrigir = Formulario.objects.filter(status=filtros_dict[filtro], capitulo=numero_cap).order_by('data_envio')
    paginator = Paginator(relatorios_corrigir, QTD_ELEMENTOS_POR_PAGINA)
    relatorios_paginados = paginator_conf(request, paginator)
    context = {"capitulos":capitulos_corrigir, "relatorios": relatorios_paginados,
                "abrir": corretor.regiao_correcao == capitulo.regiao, "corretor": corretor, "next": request.path,
                "numero_cap": capitulo.numero,
                "filtro":filtro}
    return render(request, "avaliador/avaliador_list_relatorio_cap.html", context=context)

@login_required()
def corrigir_relatorio(request, id):
    controle = controle_acesso(request)
    if controle != True:
        return controle
    if request.method == "GET":
        corretor = Gabinete_User.objects.get(user_id=request.user.id)
        capitulos_corrigir = conf_home(request, corretor)

        formulario = Formulario.objects.get(pk=id)
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
        url_redirect = request.GET.get("next", "/avaliador/home")
        context = {'form' : form, "id_relatorio":id, "capitulos": capitulos_corrigir, "corretor": corretor, "next": request.path,
                   "url_redirect":url_redirect}
        return render(request, 'avaliador/avaliador_correcao_relatorio.html', context=context)
    else:
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = Formulario.objects.get(pk=id)
            formulario.pontuacao_bonus = form.cleaned_data['pontuacaoBonus'] if form.cleaned_data['pontuacaoBonus'] != None else 0
            formulario.observacoes = form.cleaned_data['observacao']
            formulario.status = form.cleaned_data['status']
            formulario.save()
            print(request.GET.get("next", "/avaliador/home"))
            return HttpResponseRedirect(request.GET.get("next", "/avaliador/home"))

def mapa(request):
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    capitulos_corrigir = conf_home(request, corretor)
    conquistas = mapa_geral()
    context = {"capitulos": capitulos_corrigir,
                "corretor":corretor,
                "conquistas": conquistas}
    return render(request, "avaliador/avaliador_mapa_geral.html", context=context)

def mapa_cap(request, numero_cap):
    corretor = Gabinete_User.objects.get(user_id=request.user.id)
    capitulos_corrigir = conf_home(request, corretor)
    conquistas = conquista_capitulo(numero_cap)
    context = {"capitulos": capitulos_corrigir,
                "corretor":corretor,
                "conquistas": conquistas}
    return render(request, "avaliador/avaliador_mapa_cap.html", context=context)
