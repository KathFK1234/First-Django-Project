from django.db import models

# Create your models here.
class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_time = models.DateTimeField(auto_now=True)
    table_reserved = models.IntegerField(default=0)
    guest_count = models.IntegerField(default=0)