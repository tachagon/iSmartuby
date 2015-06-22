from django.conf.urls import patterns, include, url
from authen import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)