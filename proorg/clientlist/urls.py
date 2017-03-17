from django.conf.urls import url, include
from django.contrib import admin
from .views import client, clients, index, addclient, postclient, get_event_info
urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^eventsinfo/all/$', get_event_info),
    url(r'^clients/add/$', addclient),
    url(r'^client/post/$', postclient),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^', index),
]
