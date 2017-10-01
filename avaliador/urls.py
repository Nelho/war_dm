from django.conf.urls import url
from avaliador import views

urlpatterns = [
	url(r'^cadastro/$', views.cadastroAvaliador, name="cadastro_avaliador"),
]