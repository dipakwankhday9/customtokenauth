from django.shortcuts import render
from rest_framework import viewsets
from customtokenuserapp import authentication, serializer
from customtokenuserapp.models import CustomUser, CustomToken
from customtokenuserapp.serializer import CustomUserSerializer
from customtokenuserapp.authentication import CustomTokenAuthentication

# Create your views here.
class CustomUserToken(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classess = [CustomTokenAuthentication]
    
    def list(self, request, *args, **kwargs):
        print("auth",request.user.is_authenticated)
        return super().list(request, *args, **kwargs)
