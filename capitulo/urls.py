from django.conf.urls import url
from capitulo import views

urlpatterns = [
	url(r'^cadastro/', views.cadastrarCapitulo, name="cadastroCapitulo"),
	url(r'^formulario/$', views.cadastrarFormulario, name="cadastroFormulario"),
	url(r'^formulario/corrigir/(?P<id>\d+)/$', views.corrigirFormulario, name="corrigirFormulario"),

]
