from django.conf.urls import url
from mapa.views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$', territorioDetail, name="territorioDetail"),
    url(r'^mapa/$', listTerritorios, name="listTerritorios"),
    url(r'^mapa2/$', mapaTerritorios, name="listTerritorios"),

]