from django.shortcuts import render, HttpResponse
from avaliador.models import Gabinete_User
from mapa.views import mapa_geral as mapa_geral_home
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_authenticate
from django.http import HttpResponseRedirect
from main.views import redirect
from django.http import HttpResponse
import json
from capitulo.models import Capitulo_User
from mapa.views import conquista_capitulo



def mapa_inicio(request):
    conquistas = mapa_geral_home()
    context = {"conquistas": conquistas}
    return render(request, "inicio/mapa.html", context=context)

def mapa_cap(request, numero_cap):
	conquistas = conquista_capitulo(numero_cap)
	capitulo = Capitulo_User.objects.get(numero=numero_cap)
	context = {"conquistas": conquistas, "capitulo": capitulo}
	return render(request, "inicio/mapa_cap.html", context=context)

def regras_inicio(request):
    return render(request, 'inicio/regras.html')

def avaliadores(request):
	avaliadores = Gabinete_User.objects.all()
	context_dict = {'avaliadores': avaliadores}
	return render(request, 'inicio/avaliadores.html', context = context_dict)

def login_ajax(request):
	if request.is_ajax():
		mimetype = 'application/json'

		username = request.POST.get("username", None)
		passwd = request.POST.get("passwd", None)
		if (username == None) or (passwd == None):
			data = {"msg_error": "Preencha todos os campos e tente novamente", "sucesso": False}
			data = json.dumps(data)
			return HttpResponse(data, mimetype)

		user = authenticate(username=username, password=passwd)
		if user is not None:
			login_authenticate(request, user)
			url_redirect = redirect(request)
			data = {"url_redirect": url_redirect, "sucesso": True}
			data = json.dumps(data)
			return HttpResponse(data, mimetype)
		else:
			data = {"msg_error": "Login e/ou senha incorretos", "sucesso": False}
			data = json.dumps(data)
			return HttpResponse(data, mimetype)
def auto_complete(request):
	if request.is_ajax():
		mimetype = 'application/json'

		query = request.GET.get("term", "")
		capitulos = Capitulo_User.objects.filter(user__first_name__istartswith=query)
		data = []
		for capitulo in capitulos:
			cap_json = {}
			cap_json["id"] = capitulo.numero
			cap_json["label"] = capitulo.user.first_name
			cap_json["value"] = capitulo.user.first_name
			data.append(cap_json)
		data = json.dumps(data)

		return HttpResponse(data, mimetype)
