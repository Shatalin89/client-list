from django.conf.urls import url, include

from .views import client, clients, index, addclient, postclient,get_event_info, event_info_new, delevents


urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^eventsinfo/all/$', get_event_info),
    url(r'^clients/add/$', addclient),
    url(r'^eventinfo/add/$', event_info_new, name='eventinfoadd'),
    url(r'^client/post/$', postclient),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^eventinfo/del/(?P<events_info_id>\d+)/$', delevents, name='eventinfodel'),
    url(r'^', index),
]
