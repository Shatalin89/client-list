from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Clients(models.Model):
    class Meta:
        db_table = 'clients'
    clients_name = models.CharField(max_length=50)
    clients_middlename = models.CharField(max_length=50)
    clients_lastname = models.CharField(max_length=50)
    clients_age = models.DateField(null=True)
    clients_telephone = models.CharField(max_length=11)
    clients_email = models.EmailField(null=True)
    clients_comments = models.TextField()

    def get_fio(self):
        fio = self.clients_lastname+" "+self.clients_name[0]+"."+self.clients_middlename[0]+"."
        return str(fio)


class EventInfo(models.Model):
    class Meta:
        db_table = 'event_info'
    event_info_name = models.CharField(max_length = 100)
    event_info_description = models.TextField(null=True)
    event_info_poster = models.ImageField(null=True)


class Event(models.Model):
    class Meta:
        db_table = 'event'
    event_date = models.DateField(default=date.today)
    event_time = models.TimeField(default=timezone.now)
    event_infoid = models.ForeignKey(EventInfo)
    event_enable = models. BooleanField(default=False)
