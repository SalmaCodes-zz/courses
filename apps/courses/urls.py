from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]