from django.conf.urls import url, include
from django.contrib import admin
from .views import client, clients, index, addclient, postclient
from .views import get_event_info, event_info_new, del_events_info

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^eventsinfo/all/$', get_event_info),
    url(r'^clients/add/$', addclient),
    url(r'^eventinfo/add/$', event_info_new, name='eventinfoadd'),
    url(r'^client/post/$', postclient),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^eventinfo/del/(?P<events_info_id>\d+)/$', del_events_info),
    url(r'^', index),
]
