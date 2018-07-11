from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wordgen/randomize$', views.randomize),
    url(r'^wordgen/reset$', views.reset)
]