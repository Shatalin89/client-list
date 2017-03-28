from django.conf.urls import url, include
from .views import client, clients, index, addclient, postclient, client_del, client_edit, show_client_edit
from .views import event_info_edit,get_event_info, event_info_new, delevents
from .views import get_hall_info, add_hall_info, del_hall_info, edit_hall_info
from .views import get_place_info, add_place_info


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

    url(r'^hallinfo/all/$', get_hall_info, name='hallinfoall'),
    url(r'^hallinfo/add/$', add_hall_info, name='hallinfoadd'),
    url(r'^hallinfo/del/(?P<hall_info_id>\d+)/$', del_hall_info, name='hallinfodel'),
    url(r'^hallinfo/edit/(?P<hall_info_id>\d+)/$', edit_hall_info, name='hallinfoedit'),

    url(r'^placeinfo/all/$', get_place_info, name='placeinfoall'),
    url(r'^placeinfo/add/$', add_place_info, name='placeinfoadd'),

    url(r'^', index),
]
