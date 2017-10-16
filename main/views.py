from django.contrib.auth.models import User
from django.shortcuts import render
from main.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate
from django.contrib.auth import logout as logout_request
from django.http import HttpResponseRedirect
from avaliador.models import Gabinete_User
from capitulo.models import Capitulo_User

LIST_MODELS_AUTH = [[Gabinete_User, "/avaliador/home/"],
					[Capitulo_User, "/capitulo/home"]]

# Create your views here.
def login(request):
	if request.method == "POST":		
		form = LoginForm(request.POST)
		
		if form.is_valid():
			form_login = form.cleaned_data["login"]
			form_senha = form.cleaned_data["senha"]
			teste = User.objects.get(username=form_login)
			print(teste.first_name)
			user = authenticate(username=form_login, password=form_senha)

			if(user is not None):
				login_authenticate(request, user)
				redirect_url = redirect(request)
				if redirect_url != None:
					url_redirect_auth = request.GET.get("next", redirect_url)
					return HttpResponseRedirect(url_redirect_auth)

				context = {"error": True, 
				"msg_error": "Nenhum usuário cadastro no sistema!", 
				"form": form}
				return render(request, "main/login.html", context=context)
			else:
				context = {"error": True, 
				"msg_error": "Login/senha incorretos!", 
				"form": form}
				return render(request, "main/login.html", context=context)
	form = LoginForm()
	param = request.GET.get("next", None)
	login_required =  param != None
	context = {"url_redirect": param ,"form":form, "error":login_required, "msg_error": "É necessário realizar login para acessar a página solicitada!"}

	return render(request, "main/login.html", context=context)

def logout(request):
	logout_request(request)
	return HttpResponseRedirect("/")

def redirect(request):
	for models in LIST_MODELS_AUTH:
		try:
			models[0].objects.get(user_id=request.user.id)
			return models[1]
		except models[0].DoesNotExist:
			pass
	return None