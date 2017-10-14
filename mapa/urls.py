from django.conf.urls import url
from mapa.views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$', territorioDetail, name="territorioDetail"),
    url(r'^territorios/$', listTerritorios, name="listTerritorios"),


]