from django.contrib import admin
from clientlist.models import Clients

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fields = ['clients_name','clients_middlename','clients_lastname','clients_age','clients_telephone',
              'clients_email']

admin.site.register(Clients, ClientAdmin)