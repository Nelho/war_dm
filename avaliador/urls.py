from django.conf.urls import url
from avaliador import views

urlpatterns = [
	url(r'^cadastro/$', views.cadastro_avaliador, name="cadastro_avaliador"),
	url(r'^profile/$', views.profile_avaliador, name="profile_avaliador"),
	url(r'^edit/profile$', views.profile_edit, name="profile_edit"),
	url(r'^edit/password$', views.password_edit, name="password_edit")
	
]