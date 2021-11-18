from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#models
from .models import Room

#serializers
from .serializers import RoomSerializer

class RoomsViewset(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filterset_fields = ["type"]
    filter_backends = [DjangoFilterBackend]