from django.conf.urls import url
from capitulo import views

urlpatterns = [
	url(r'^cadastro/', views.cadastrarCapitulo, name="cadastroCapitulo"),
	url(r'^formulario/(?P<id>\d+)/$', views.cadastrarFormulario, name="cadastroFormulario"),

]
