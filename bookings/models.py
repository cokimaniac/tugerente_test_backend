from django.db import models

#models
from clients.models import Client

class Booking(models.Model):
    STATE_CHOICES = (
        ("PEND", "Pending"),
        ("PAID", "Paid"),
        ("REMO", "Removed")
    )
    payment_ammount = models.FloatField(default=0.0)
    total_to_pay = models.FloatField(default=0.0)
    state = models.CharField(
        choices=STATE_CHOICES,
        default="PEND",
        max_length=15
    )
    stay_days = models.IntegerField(
        default=None,
    )
    reserved_at = models.DateTimeField(
        auto_now=True
    )
    reserved_for = models.DateTimeField(
        auto_now_add=False
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def reserved_by(self):
        return self.client