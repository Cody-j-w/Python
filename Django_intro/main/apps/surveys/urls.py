from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^surveys$', views.list),
    url(r'^surveys/new$', views.new),

]