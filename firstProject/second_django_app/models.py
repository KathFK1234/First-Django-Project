from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    reservation_date = models.DateField
    reservation_time = models.DateTimeField
    table_reserved = models.IntegerField
    guests = models.IntegerField