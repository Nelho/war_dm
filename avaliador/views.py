from django.shortcuts import render
from avaliador.forms import AvaliadorForm
from django.contrib.auth.models import User
from main.models import Usuario
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from main.models import Contato
from django.http import HttpResponseRedirect


# Create your views here.
def cadastroAvaliador(request):
	if request.method == "POST":
		form = AvaliadorForm(request.POST, request.FILES)
		if form.is_valid():
			form_senha = form.cleaned_data["senha"]
			form_confirmar_senha = form.cleaned_data["confirmar_senha"]
			if form_senha != form_confirmar_senha:
				context = {"form": form}
				return render(request, "avaliador/cadastro_avaliador.html", context=context)
			form_nome = form.cleaned_data["nome"]
			form_login = form.cleaned_data["login"]
			form_regiao = form.cleaned_data["regiao"]
			form_email = form.cleaned_data["email"]
			form_telefone = form.cleaned_data["telefone"]
			TIPO_USUARIO = "AVA"
			form_foto = request.FILES["foto"]
			#form_foto.name = form_login + form_foto.name[form_foto.name.find("."):]

			new_user = User.objects.create_user(form_login, password=form_senha, 
				first_name=form_nome, email=form_email)
			new_user.save()
			new_usuario = Usuario(user=new_user, 
				regiao=form_regiao,
				tipoUsuario=TIPO_USUARIO,
				foto=form_foto)
			new_usuario.save()
			new_contato = Contato(usuario=new_user, contato=form_telefone)
			new_contato.save()

			return HttpResponseRedirect('/avaliador/cadastro')

	form = AvaliadorForm()
	context = {"form": form}
	return render(request, "avaliador/cadastro_avaliador.html", context=context)
