from django.contrib import admin
from .models import Clients, EventInfo, Event

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fields = ['clients_name','clients_middlename','clients_lastname','clients_age','clients_telephone',
              'clients_email']



admin.site.register(EventInfo)
admin.site.register(Clients, ClientAdmin)
admin.site.register(Event)