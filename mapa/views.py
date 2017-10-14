from django.shortcuts import render
from mapa.models import Territorio

# Create your views here.

def listTerritorios(request):
    territorios = Territorio.objects.all()
    context = {"territorios": territorios}
    return render(request, "mapa/war_territorios.html", context=context)

def territorioDetail(request, id):
    territorio = Territorio.objects.get(pk=id)
    print(territorio.descricao)
    context = {"territorio" : territorio}
    return render(request,"mapa/territorio_detail.html", context=context)

def mapaTerritorios(request):
    territorios = Territorio.objects.all()
    context = {"brasil": territorios[0], "Japao" : territorios[1]}
    return render(request, "mapa/war_territorios2.html", context=context)