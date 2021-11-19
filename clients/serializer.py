from rest_framework import serializers

#models
from .models import Client

class ClientSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True, 
        write_only=True,
        style={"input_type": "password"}
    )

    def create(self, validated_data):
        password = validated_data.pop("password")
        client = Client.objects.create(**validated_data)
        client.set_password(password)
        client.save()
        return client