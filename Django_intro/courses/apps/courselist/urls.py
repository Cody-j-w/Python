from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses/$', views.index),
    url(r'^courses/create/$', views.create),
    url(r'^courses/(?P<id>\d+)$', views.course),
    url(r'^courses/(?P<id>\d+)/comment$', views.comment),
    url(r'^courses/(?P<id>\d+)/delete$', views.delete),
    url(r'^courses/(?P<id>\d+)/destroy$', views.destroy),
]