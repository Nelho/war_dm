from django.conf.urls import url
from avaliador import views

urlpatterns = [
	url(r'^cadastro/$', views.cadastro_avaliador, name="cadastro_avaliador"),
	url(r'^home/$', views.avaliador_home, name="avaliador_home"),
	url(r'^edit/profile$', views.profile_edit, name="profile_edit"),
	url(r'^edit/password$', views.password_edit, name="password_edit"),
	url(r'^cap/(?P<numero_cap>[0-9]+)/$', views.avaliar_cap, name="cap_numero"),
	url(r'^relatorio/(?P<id>\d+)/$', views.corrigir_relatorio, name="corrigir_relatorio"),
	url(r'^mapa/$', views.mapa, name="mapa_avaliador")
	
]