from django.shortcuts import render
from mapa.models import Territorio

# Create your views here.

def listTerritorios(request):
    territorios = Territorio.objects.all()
    context = {"territorios": territorios}
    return render(request, "mapa/list_territorios.html", context=context)

def territorioDetail(request, id):
    territorio = Territorio.objects.get(pk=id)
    print(territorio.descricao)
    context = {"territorio" : territorio}
    return render(request,"mapa/territorio_detail.html", context=context)