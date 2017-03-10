from django.conf.urls import url, include
from django.contrib import admin
from clientlist.views import  client, clients
urlpatterns = [
    url(r'^clients/all/$', clients),
    #url(r'^clients/get/(?<clients_id>)\d+/$', client),

]
