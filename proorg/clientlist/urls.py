from django.conf.urls import url, include
from .views import client, clients, index, addclient, postclient, client_del, client_edit, show_client_edit
from .views import event_info_edit,get_event_info, event_info_new, delevents


urlpatterns = [
    url(r'^clients/all/$', clients),
    url(r'^clients/add/$', addclient),
    url(r'^client/post/$', postclient),
    url(r'^clients/get/(?P<clients_id>\d+)/$', client),
    url(r'^client/del/(?P<clients_id>\d+)/$', client_del, name='clientdel'),
    url(r'^client/edit/(?P<clients_id>\d+)/$', client_edit, name='client_edit'),
    url(r'^client/edit/show/(?P<clients_id>\d+)/$', show_client_edit, name='show_client_edit'),

    url(r'^eventsinfo/all/$', get_event_info),
    url(r'^eventinfo/add/$', event_info_new, name='eventinfoadd'),
    url(r'^eventinfo/edit/(?P<events_info_id>\d+)/$', event_info_edit, name='event_info_edit'),
    url(r'^eventinfo/del/(?P<events_info_id>\d+)/$', delevents, name='eventinfodel'),

    url(r'^', index),
]
