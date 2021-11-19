"""
room serializers.
"""

from rest_framework import serializers
# models
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ["availability"]
        model = Room