from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

# models
from bookings.models import Booking
from rooms.models import Room

#serializers
from .serializers import BookingListSerializer, BookingSerializer

class RegisterBookingView(APIView):

    permission_classes = [IsAuthenticated]
    
    def post (self, request):
        data = {
            "room": request.GET.get("room"),
            "client": request.user.email
        }
        room = Room.objects.get(id=request.GET.get("room"))
        data.update(request.data)
        serialized = BookingSerializer(data=data)
        if serialized.is_valid():
            if room.availability:
                serialized.save()
                return Response({
                    "booking": serialized.data
                })
            return Response({
                "error": "Room is not available"
            })
        return Response({
            "errors": serialized.errors
        })

class BookingListView(ListAPIView):
    serializer_class = BookingListSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]