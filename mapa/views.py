from django.shortcuts import render
from mapa.models import Territorio
from capitulo.models import Formulario, Capitulo_User


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
# [{"pontuacao": 10, "pontuacao_bonus": 10, "territorio": Territorio}]


def mapa_geral():
    territorios = Territorio.objects.all()
    capitulos = Capitulo_User.objects.all()
    cont = 0
    resultado = {}
    for territorio in territorios:
        resultado[territorio.nome] = []
        for capitulo in capitulos:
            relatorios = Formulario.objects.filter(capitulo=capitulo.numero, status="S1", territorio=territorio.id)
            soma_pontuacao_bonus = 0
            for relatorio in relatorios:
                soma_pontuacao_bonus += relatorio.pontuacao_bonus
            print(relatorios.count())
            if(relatorios.count() != 0):
                if cont == 0:
                    cont += 1
                    resultado[territorio.nome].append({"capitulo": capitulo, "pontuacao": soma_pontuacao_bonus, "territorio" : territorio})
                else:
                    if soma_pontuacao_bonus > resultado[territorio.nome][0]["pontuacao"]:
                        resultado[territorio.nome] = {"capitulo": capitulo, "pontuacao": soma_pontuacao_bonus, "territorio" : territorio}
                    elif soma_pontuacao_bonus == resultado[territorio.nome][0]["pontuacao"]:
                        resultado[territorio.nome].append({"capitulo": capitulo, "pontuacao": soma_pontuacao_bonus, "territorio" : territorio})
        cont = 0
    return resultado