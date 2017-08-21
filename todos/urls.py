from django.conf.urls import url
from . import views # the . is current director

urlpatterns = [
    url(r'^$', views.index, name='index'), # ^ is start with, $ is ends with
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add', views.add, name="add")
]