from django.conf.urls import url
from capitulo import views

urlpatterns = [
	url(r'^cadastro/', views.cadastrarCapitulo, name="cadastroCapitulo"),
	url(r'^formulario/(?P<id>\d+)/$', views.cadastrarRelatorio, name="cadastroFormulario"),
	url(r'^home/', views.home, name="capituloHome"),

]
