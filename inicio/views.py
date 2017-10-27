from django.shortcuts import render, HttpResponse

def mapa_inicio(request):
    return render(request, 'inicio/mapa.html')

def regras_inicio(request):
    return render(request, 'inicio/regras.html')

def avaliadores(request):
	return render(request, 'inicio/avaliadores.html')
