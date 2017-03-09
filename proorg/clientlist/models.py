from django.db import models

# Create your models here.
class Clients(models.Model):
    class Meta:
        db_table = 'clients'
    clients_name = models.CharField(max_length=50)
    clients_middlename = models.CharField(max_length=50)
    clients_lastname = models.CharField(max_length=50)
    clients_age = models.DateField(null=True)
    clients_telephone = models.CharField(max_length=11)
    clients_comments = models.TextField()
