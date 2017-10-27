from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^mapa/', views.mapa_inicio, name='mapa_inicio'),
    url(r'^regras/', views.regras_inicio, name='regras_inicio'),
    url(r'^avaliadores/', views.avaliadores, name='avaliadores'),
]