from django.shortcuts import render
from login.forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate

# Create your views here.
def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		
		if form.is_valid():
			form_login = form.cleaned_data['login']
			form_senha = form.cleaned_data["senha"]
			user = authenticate(username=form_login, password=form_senha)

			if(user is not None):
				login_authenticate(request, user)
				return HttpResponse(request, user.username)
			else:
				context = {"error": True, 
				"msg_error": "Login/senha incorretos!", 
				"form": form}
				return render(request, "login/login.html", context=context)
	form = LoginForm()
	context = {"form":form}

	return render(request, "login/login.html", context=context)