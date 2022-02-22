from rest_framework import  serializers
from customtokenuserapp.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "token"]
    