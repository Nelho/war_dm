from django.shortcuts import render
from mapa.models import Territorio
from capitulo.models import Formulario

# Create your views here.
def conquista_capitulo(numero_cap):
    territorios = Territorio.objects.all()
    conquistas = []
    for territorio in territorios:
        relatorios = Formulario.objects.filter(capitulo=numero_cap, status="S1", territorio=territorio.id)
        if relatorios.count() >= 1:
            pacote = {"territorio": territorio}
            pontuacao_bonus = 0
            for relatorio in relatorios:
                pontuacao_bonus += relatorio.pontuacao_bonus
            pacote["pontuacao_bonus"] = pontuacao_bonus
            pacote["pontuacao"] = territorio.pontuacao
            conquistas.append(pacote)
    return conquistas


