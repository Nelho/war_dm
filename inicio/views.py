from django.shortcuts import render, HttpResponse

def mapa_inicio(request):
    return render(request, 'inicio/mapa.html')
