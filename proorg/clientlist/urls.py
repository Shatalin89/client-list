from django.conf.urls import url, include
from django.contrib import admin
from clientlist.views import client, clients, index, addclient, postclient
urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^clients/add/$', addclient),
    url(r'^client/post/$', postclient),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^', index),
]
