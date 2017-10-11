from django.shortcuts import render
from main.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate
from django.contrib.auth import logout as logout_request
from django.http import HttpResponseRedirect
from avaliador.models import Gabinete_User
from capitulo.models import Capitulo_User

LIST_MODELS_AUTH = [[Gabinete_User, "/avaliador/profile/"],
					[Capitulo_User, "/"]]

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
				for models in LIST_MODELS_AUTH:
					try:
						models[0].objects.get(user_id=request.user.id)
						return HttpResponseRedirect(models[1])
					except:
						print("Nao deu redirect")
				#usuario = Gabinete_User.objects.get(user_id=request.user.id)
				#if usuario.tipoUsuario == "AVA":
				#	return HttpResponseRedirect("/avaliador/profile")
					#return HttpResponse(user)
			else:
				context = {"error": True, 
				"msg_error": "Login/senha incorretos!", 
				"form": form}
				return render(request, "main/login.html", context=context)
	form = LoginForm()
	context = {"form":form}

	return render(request, "main/login.html", context=context)

def logout(request):
	logout_request(request)
	return HttpResponseRedirect("/")