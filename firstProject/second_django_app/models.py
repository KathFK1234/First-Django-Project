from django.db import models
from datetime import date

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    contact = models.IntegerField(default='0700000000')
    tables_reserved = models.IntegerField(default='0')
    guest_count = models.IntegerField(default='0')
    reservation_date = models.DateField(default=date.today())
    reservation_time = models.DateField(auto_now=True)