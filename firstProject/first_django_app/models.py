from django.db import models

# Create your models here.
# They are created by inheriting from the models class
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)