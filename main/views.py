from django.shortcuts import render
from main.forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate
from django.contrib.auth import logout as logout_request
from django.http import HttpResponseRedirect
from main.models import Usuario

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
				usuario = Usuario.objects.get(user_id=request.user.id)
				if usuario.tipoUsuario == "AVA":
					return HttpResponseRedirect("/avaliador/profile")
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