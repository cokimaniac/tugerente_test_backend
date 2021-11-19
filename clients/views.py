#django
from django.contrib.auth import authenticate

#DRF
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

#models
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

class LoginClientView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        client = authenticate(username=email, password=password)
        
        if not client:
            return Response({
                "error": "Login failed"
            })
        
        token, _ = Token.objects.get_or_create(user=client)
        return Response({
            "token": token.key
        })