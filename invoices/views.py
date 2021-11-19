from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# models
from clients.models import Client
from rooms.models import Room
from bookings.models import Booking
from invoices.models import Invoice

#serializers
from .serializers import InvoiceSerializer

import json

class CreateInvoiceView (APIView):

    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        booking_ids = request.GET.get("booking_ids").split(",")
        bookings = []
        invoice = {}
        ammount = 0
        client = Client.objects.get(email=request.user)
        for id in booking_ids:
            booking = Booking.objects.get(id=id)
            room = Room.objects.get(booking=booking)
            ammount += room.price
            bookings.append({
                "type": room.type,
                "details": room.details,
                "price": room.price
            })
        invoice.update({
            "bookings": bookings,
            "client_name": client.get_fullname(),
            "ammount": ammount,
            "nit": request.data.get("nit")
        })
        serialized = InvoiceSerializer(data=invoice)
        if serialized.is_valid():
            return Response({
                "invoice": serialized.data
            })
        return Response({
            "errors": serialized.errors
        })
