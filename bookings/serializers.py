from rest_framework import serializers

#models
from clients.models import Client
from rooms.models import Room
from bookings.models import Booking

class BookingListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingSerializer(serializers.Serializer):
    stay_days = serializers.IntegerField(required=True)
    reserved_for = serializers.DateTimeField(required=True)
    client = serializers.CharField(required=True)
    room = serializers.CharField(required=True)
    payment_ammount = serializers.FloatField()

    def create(self, validated_data):
        room_id = validated_data.get("room")
        client_email = validated_data.pop("client")
        payment_ammount = validated_data.get("payment_ammount")

        client = Client.objects.get(email=client_email)
        room = Room.objects.get(id=room_id)

        total_to_pay = room.price - payment_ammount

        validated_data.update({"client": client, "total_to_pay": total_to_pay})

        if payment_ammount == room.price:
            validated_data.update({"state": "PAID"})
        elif payment_ammount < room.price:
            validated_data.update({"state": "PEND"})

        booking = Booking.objects.create(**validated_data)
        booking.save()
        room.booking = booking
        room.availability = False
        room.save()
        return booking