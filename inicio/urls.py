from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^mapa/', views.mapa_inicio, name='mapa_inicio'),
    url(r'^cap/(?P<numero_cap>[0-9]+)/mapa/$', views.mapa_cap, name="inicio_mapa_cap"),
    url(r'^regras/', views.regras_inicio, name='regras_inicio'),
    url(r'^avaliadores/', views.avaliadores, name='avaliadores'),
    url(r'^login/$', views.login_ajax, name="login_ajax"),
    url(r'^autocomplete/$', views.auto_complete, name="auto_complete")
]