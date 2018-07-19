from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.the_wall),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^create_message$', views.create_message),
    url(r'^like$', views.like),
    url(r'^delete_message$', views.delete_message),
    url(r'^logout$', views.logout),
    url(r'^poplist$', views.poplist)
]