from django.db import models

from bookings.models import Booking

class Room (models.Model):
    TYPE_CHOICES = (
        ("IND", "Individual"),
        ("TWIN", "Twin"),
        ("DOUB", "Doubble"),
        ("TRIP", "Triple"),
        ("QUAD", "Quadruple"),
        ("ROOM", "Entire Room")
    )

    details = models.TextField(blank=False)
    type = models.CharField(
        blank=False, 
        max_length=20, 
        choices=TYPE_CHOICES
    )
    availability = models.BooleanField(
        default=True
    )
    price = models.FloatField(null=False)
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
    )