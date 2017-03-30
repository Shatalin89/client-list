from django.contrib import admin
from  clientlist import models

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fields = ['clients_name','clients_middlename','clients_lastname','clients_age','clients_telephone',
              'clients_email']


admin.site.register(models.EventInfo)
admin.site.register(models.Clients, ClientAdmin)
admin.site.register(models.Event)
admin.site.register(models.Hall)
admin.site.register(models.PlaceInfo)
admin.site.register(models.PlaceScheme)
admin.site.register(models.StatusPlace)
admin.site.register(models.EventPlacePrice)
admin.site.register(models.TypeScheme)
admin.site.register(models.PlaceSector)
