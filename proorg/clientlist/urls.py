from django.conf.urls import url, include
from django.contrib import admin
from clientlist.views import client, clients, index
urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^', index),
]
