from django.db import models

from clients.models import Client
from rooms.models import Room
from bookings.models import Booking

class Invoice(models.Model):
    nit = models.CharField(max_length=20)
    ammount = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bookings = models.CharField(max_length=50)
