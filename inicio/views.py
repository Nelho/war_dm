from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'inicio/tela_inicial.html')
