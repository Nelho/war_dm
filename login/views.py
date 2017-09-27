from django.shortcuts import render
from login.forms import LoginForm, AvaliadorForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate
from django.contrib.auth.models import User
from login.models import Usuario
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		
		if form.is_valid():
			form_login = form.cleaned_data["login"]
			form_senha = form.cleaned_data["senha"]
			user = authenticate(username=form_login, password=form_senha)

			if(user is not None):
				login_authenticate(request, user)

				return HttpResponse(user)
			else:
				context = {"error": True, 
				"msg_error": "Login/senha incorretos!", 
				"form": form}
				return render(request, "login/login.html", context=context)
	form = LoginForm()
	context = {"form":form}

	return render(request, "login/login.html", context=context)

def cadastroAvaliador(request):
	if request.method == "POST":
		form = AvaliadorForm(request.POST, request.FILES)
		if form.is_valid():
			form_nome = form.cleaned_data["nome"]
			form_sobrenome = form.cleaned_data["sobrenome"]
			form_login = form.cleaned_data["login"]
			form_senha = form.cleaned_data["senha"]
			form_regiao = form.cleaned_data["regiao"]
			form_email = form.cleaned_data["email"]
			form_telefone = form.cleaned_data["telefone"]
			TIPO_USUARIO = "AVA"
			form_foto = request.FILES["foto"]
			#form_foto.name = form_login + form_foto.name[form_foto.name.find("."):]
			print(form_senha)


			new_user = User.objects.create_user(form_login, password=form_senha, 
				first_name=form_nome,
				last_name=form_sobrenome)
			new_user.save()
			new_usuario = Usuario(user=new_user, 
				regiao=form_regiao,
				tipoUsuario=TIPO_USUARIO,
				foto=form_foto)

			new_usuario.save()
			return HttpResponse("pegou")

	form = AvaliadorForm()
	context = {"form": form}
	return render(request, "login/cadastro_avaliador.html", context=context)

def cadastroCapitulo(request):
	return render(request, "login/cadastro_capitulo.html")

def gerenciaInicio(request):
	return render(request, "login/../templates/base_html_gerente.html")
