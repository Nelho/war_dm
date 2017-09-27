from django.conf.urls import url
from avaliacao import views

urlpatterns = [
	url(r'^index$', views.index, name="index")
]