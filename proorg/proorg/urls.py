from django.conf.urls import url, include
from django.contrib import admin
from clientlist import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('clientlist.urls')),
    url(r'^', include('clientlist.urls')),
]


