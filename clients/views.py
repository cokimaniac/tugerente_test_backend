from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from clients.models import Client

# serializers
from .serializer import ClientSerializer

class SignupClientView(APIView):

    def post(self, request):
        pass_confirmation = request.data.pop("pass_confirmation")
        serialized = ClientSerializer(data=request.data)
        if serialized.is_valid():
            password = serialized.validated_data.get("password")
            if pass_confirmation == password:
                serialized.save()
                return Response(serialized.data)
            return Response({"error": "Password confirmation failed"}, status=400)
        return Response({ "error": serialized.errors })
