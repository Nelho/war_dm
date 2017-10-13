from django.shortcuts import render
from avaliador.forms import AvaliadorForm, AvaliadorEditForm, AvaliadorEditPasswordForm
from django.contrib.auth.models import User
from avaliador.models import Gabinete_User
from capitulo.models import Capitulo_User, Formulario
from main.models import Contato
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import login


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
            new_user = User.objects.create_user(form_login, password=form_senha,
                                        first_name=form_nome, last_name=form_sobrenome, email=form_email)
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

# função criada para reutilização de código. Ela busca os capítulos e
# quantos relatórios ele possui
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

def avaliador_home(request):
    corretor = Gabinete_User.objects.get(id=request.user.id)
    capitulos_corrigir = conf_home(request, corretor)
    print(corretor.foto.url)
    relatorios_corrigir = Formulario.objects.filter(capitulo__regiao=corretor.regiao_correcao, status='S4').only('capitulo').order_by('data_envio') # '-data_envio'
    context = {"capitulos":capitulos_corrigir, "relatorios": relatorios_corrigir, "corretor": corretor}
    return render(request, "avaliador/avaliador_home.html", context=context)

def avaliar_cap(request, numero_cap):
    corretor = Gabinete_User.objects.get(id=request.user.id)
    capitulo = Capitulo_User.objects.get(numero=numero_cap)
    capitulos_corrigir = conf_home(request, corretor)
    relatorios_corrigir = Formulario.objects.filter(status='S4', capitulo=numero_cap).order_by('data_envio')
    context = {"capitulos":capitulos_corrigir, "relatorios": relatorios_corrigir,
                "abrir": corretor.regiao_correcao == capitulo.regiao}
    return render(request, "avaliador/avaliador_cap.html", context=context)


def profile_edit(request):
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

    context = {"form": form, "capitulos":capitulos_corrigir}
    return render(request, "avaliador/avaliador_edit_profile.html", context=context)


def password_edit(request):
    usuario = Gabinete_User.objects.get(user_id=request.user.id)
    capitulos_corrigir = conf_home(request, usuario)
    if request.method == "POST":
        form = AvaliadorEditPasswordForm(request.POST)
        if form.is_valid():
            form_senha_atual = form.cleaned_data["senha_atual"]
            form_nova_senha = form.cleaned_data["nova_senha"]
            form_repetir_senha = form.cleaned_data["repetir_senha"]

            if form_nova_senha != form_repetir_senha:
                senha_validada = False
                # msg_error = "Senhas diferentes!"
                context = {"form": form, "error": True, "msg_error": "Senhas diferentes!", "capitulos":capitulos_corrigir}
                return render(request, "avaliador/avaliador_edit_password.html", context=context)
            else:
                user = User.objects.get(pk=request.user.id)

                if user.check_password(form_senha_atual):
                    user.set_password(form_nova_senha)
                    user.save()
                    login(request, user)
                    senha_validada = True
                    context = {"form": form, "senha_validada": senha_validada, "method": "POST", "capitulos":capitulos_corrigir}
                    return render(request, "avaliador/avaliador_edit_password.html", context=context)
                else:
                    senha_validada = False
                    context = {"form": form, "error": True, "msg_error": "Senha atual incorreta!", "capitulos":capitulos_corrigir}

                return render(request, "avaliador/avaliador_edit_password.html", context=context)
    form = AvaliadorEditPasswordForm()
    senha_validada = True
    context = {"form": form, "senha_validada": senha_validada, "method": "GET", "capitulos":capitulos_corrigir}

    return render(request, "avaliador/avaliador_edit_password.html", context=context)
