from django.db import models
from datetime import date
from django.utils import timezone
from djmoney.models.fields import MoneyField
from datetime import datetime
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
    event_info_description = models.TextField(blank=True)
    event_info_poster = models.ImageField(upload_to='image/', blank=True)
    data_add = models.DateField(default=timezone.now, blank=True, null=True)


class Event(models.Model):
    class Meta:
        db_table = 'event'
    event_infoid = models.ForeignKey(EventInfo)
    event_date = models.DateField(default=date.today)
    event_time = models.TimeField(default=timezone.now)
    event_enable = models.BooleanField(default=False)


class Hall(models.Model):
    class Meta:
        db_table = 'hall'
    hall_name = models.CharField(max_length = 100)
    hall_address = models.CharField(max_length = 100, blank = True)
    hall_max_places = models.IntegerField(default=10, blank = True, null=True)

    def __str__(self):
        return self.hall_name


class TypeScheme(models.Model):
    class Meta:
        db_table = 'type_scheme'
    type_scheme_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.type_scheme_name


class PlaceInfo(models.Model):
    class Meta:
        db_table = 'place_info'
    place_scheme_name = models.CharField(max_length = 100)
    place_sheme_hall = models.ForeignKey(Hall, blank=True, null=True)
    place_type_scheme = models.ForeignKey(TypeScheme)
    place_flag_set_sceme = models.BooleanField(default=False)
    place_current_count = models.IntegerField(blank=True, null=True)


class PlaceSector(models.Model):
    class Meta:
        db_table = 'place_sector'
    sector_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.sector_name

class PlaceScheme(models.Model):
    class Meta:
        db_table = 'place_scheme'
    place_name = models.CharField(max_length = 20, default='Входной')
    place_raw = models.IntegerField(blank=True, null=True)
    place_places = models.IntegerField(blank=True, null=True)
    place_x = models.IntegerField(blank=True, null=True)
    place_y = models.IntegerField(blank=True, null=True)
    place_sector = models.ForeignKey(PlaceSector, default=1)
    place_scheme_id = models.ForeignKey(PlaceInfo, blank=True, null=True)

    def __str__(self):
        return self.place_scheme_id.place_scheme_name +' '+self.place_name



class StatusPlace(models.Model):
    class Meta:
        db_table = 'status_place'
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return self.status_name

class EventPlacePrice(models.Model):
    class Meta:
        db_table = 'event_place_price'
    epp_event = models.ForeignKey(Event)
    epp_place = models.ForeignKey(PlaceInfo, blank=True, null=True)
    epp_place_scheme = models.ForeignKey(PlaceScheme, blank=True, null=True)
    epp_place_status = models.ForeignKey(StatusPlace)
    epp_client = models.ForeignKey(Clients)
    epp_place_price = MoneyField(max_digits=10, decimal_places=2, default_currency='RUB')
    epp_place_made_price = MoneyField(max_digits=10, decimal_places=2, default_currency='RUB')
    epp_datetime_price = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.epp_event



