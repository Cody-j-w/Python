from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/randomize$', views.randomize),
    url(r'^/reset$', views.reset)
]