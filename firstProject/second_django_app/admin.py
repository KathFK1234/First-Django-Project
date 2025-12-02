from django.contrib import admin
from .models import Reservation # This imports the model we created for the app

# Register your models here.
admin.site.register(Reservation)