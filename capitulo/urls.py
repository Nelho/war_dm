from django.conf.urls import url
from capitulo import views

urlpatterns = [
	url(r'^cadastro/', views.cadastrarCapitulo, name="cadastroCapitulo"),
	url(r'^formulario/(?P<id>\d+)/$', views.cadastrarRelatorio, name="cadastroFormulario"),
	url(r'^home/$', views.home, name="capituloHome"),
	url(r'^edit/$', views.edit, name='editar_cap'),
	url(r'^senha/$', views.alterarSenha, name='edit_senha'),
	url(r'^regras/$', views.regras, name='regras'),
	url(r'^avaliadores/$', views.avaliadores, name='avaliadores'),
	url(r'^legenda/$', views.legenda_territorios, name="legenda_territorios")

]
