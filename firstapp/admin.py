from django.contrib import admin
from .models import Reservation  # we impoert reservation
# Register your models here.

# to register our model and pass in the name of our model reservation.
admin.site.register(Reservation)
# we need to make migrations to create table in our database.
