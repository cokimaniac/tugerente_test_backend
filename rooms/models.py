from django.db import models

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
    price = models.FloatField()

    def __init__ (self):
        return self.type