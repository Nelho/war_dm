from django.conf.urls import url
from main import views

urlpatterns = [
	url(r'^$', views.login, name="login"),
	url(r'logout/$', views.logout ,name="logout")
]