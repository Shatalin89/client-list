from django.conf.urls import url, include
from django.contrib import admin
from clientlist import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('clientlist.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


