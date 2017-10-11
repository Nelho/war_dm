from django.shortcuts import render
from avaliador.forms import AvaliadorForm, AvaliadorEditForm, AvaliadorEditPasswordForm
from django.contrib.auth.models import User
from avaliador.models import Gabinete_User
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
            form_nome = form.cleaned_data["nome"]
            form_sobrenome = form.cleaned_data["sobrenome"]
            form_login = form.cleaned_data["login"]
            form_senha = form_login + "_" + form_nome
            form_regiao = form.cleaned_data["regiao"]
            form_email = form.cleaned_data["email"]
            form_telefone = form.cleaned_data["telefone"]
            form_regiao_correcao = form.cleaned_data["regiao_correcao"]
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
            new_contato = Contato(usuario=new_user, contato=form_telefone)
            new_contato.save()

            # return HttpResponseRedirect('/avaliador/cadastro')
            cadastro = True


    form = AvaliadorForm()
    context = {"form": form, "cadastro": cadastro }
    return render(request, "avaliador/cadastro_avaliador.html", context=context)


def profile_avaliador(request):
    return render(request, "avaliador/avaliador_profile.html")


def profile_edit(request):
    if request.method == "POST":
        form = AvaliadorEditForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            usuario = Gabinete_User.objects.get(user_id=request.user.id)

            form_nome = form.cleaned_data["nome"]
            form_sobrenome = form.cleaned_data["sobrenome"]
            form_email = form.cleaned_data["email"]
            form_telefone = form.cleaned_data["telefone"]
            form_regiao = form.cleaned_data["regiao"]
            try:
                form_foto = request.FILES["foto"]
            except MultiValueDictKeyError:
                form_foto = usuario.foto

            user.first_name = form_nome
            user.last_name = form_sobrenome
            user.email = form_email

            usuario.foto = form_foto
            usuario.regiao = form_regiao

            ##contato.contato = form_telefone

            user.save()
            usuario.save()
            ##contato.save()
            return HttpResponseRedirect('/avaliador/profile')
    elif request.method == "GET":
        usuario = Gabinete_User.objects.get(user_id=request.user.id)
        user = User.objects.get(pk=request.user.id)
        form_initial = {"nome": user.first_name,
                        "sobrenome": user.last_name,
                        "email": user.email, "regiao": usuario.regiao}
        try:
            contato = Contato.objects.get(usuario_id=request.user.id)
            form_initial["contato"] = contato.contato
        except:
            print("Contato não cadastrado para usuário")

        form = AvaliadorEditForm(initial=form_initial)

    context = {"form": form}
    return render(request, "avaliador/avaliador_edit_profile.html", context=context)


def password_edit(request):
    if request.method == "POST":
        form = AvaliadorEditPasswordForm(request.POST)
        if form.is_valid():
            form_senha_atual = form.cleaned_data["senha_atual"]
            form_nova_senha = form.cleaned_data["nova_senha"]
            form_repetir_senha = form.cleaned_data["repetir_senha"]

            if form_nova_senha != form_repetir_senha:
                senha_validada = False
                # msg_error = "Senhas diferentes!"
                context = {"form": form, "error": True, "msg_error": "Senhas diferentes!"}
                return render(request, "avaliador/avaliador_edit_password.html", context=context)
            else:
                user = User.objects.get(pk=request.user.id)

                if user.check_password(form_senha_atual):
                    user.set_password(form_nova_senha)
                    user.save()
                    login(request, user)
                    senha_validada = True
                    context = {"form": form, "senha_validada": senha_validada, "method": "POST"}
                    return render(request, "avaliador/avaliador_edit_password.html", context=context)
                else:
                    senha_validada = False
                    context = {"form": form, "error": True, "msg_error": "Senha atual incorreta!"}

                return render(request, "avaliador/avaliador_edit_password.html", context=context)
    form = AvaliadorEditPasswordForm()
    senha_validada = True
    context = {"form": form, "senha_validada": senha_validada, "method": "GET"}

    return render(request, "avaliador/avaliador_edit_password.html", context=context)
