from django.shortcuts import render, HttpResponse
from avaliador.models import Gabinete_User
from mapa.views import mapa_geral as mapa_geral_home


def mapa_inicio(request):
    conquistas = mapa_geral_home()
    context = {"conquistas": conquistas}
    return render(request, "inicio/mapa.html", context=context)

def regras_inicio(request):
    return render(request, 'inicio/regras.html')

def avaliadores(request):
	avaliadores = Gabinete_User.objects.all()
	context_dict = {'avaliadores': avaliadores}
	return render(request, 'inicio/avaliadores.html', context = context_dict)

