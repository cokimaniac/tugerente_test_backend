from rest_framework import serializers

class InvoiceSerializer(serializers.Serializer):
    client_name = serializers.CharField()
    ammount = serializers.FloatField()
    nit = serializers.CharField()
    bookings = serializers.ListField()