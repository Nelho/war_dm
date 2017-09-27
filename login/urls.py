from django.conf.urls import url
from login import views

urlpatterns = [
	url(r'^$', views.login, name="login"),
	url(r'^cadastro/avaliador$', views.cadastroAvaliador, name="cadastro_avaliador"),
	url(r'^cadastro/capitulo$', views.cadastroCapitulo, name="cadastro_capitulo"),
	url(r'^gerencia/inicio$', views.gerenciaInicio, name="gerenciaInicio")
]