from django.conf.urls import url
from capitulo import views

urlpatterns = [
	url(r'^cadastro/', views.cadastrarCapitulo, name="cadastroCapitulo")
]
