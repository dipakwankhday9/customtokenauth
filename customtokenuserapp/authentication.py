
from rest_framework import authentication
from rest_framework import exceptions

from customtokenuserapp.models import CustomToken, CustomUser
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    model = CustomToken
    
    def authenticate(self,request):
        #we want to authenticate any incoming request as the user given by the username in a custom request header named 'HTTP_AUTHORIZATION'.
        
        if request.META.get('HTTP_AUTHORIZATION') != None and request.META['HTTP_AUTHORIZATION'].startswith("Bearer "):
            userToken = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            try:
                user =CustomUser.objects.get(token=userToken) # get the user
            except CustomUser.DoesNotExist:
                # raise exception if user does not exist 
                raise exceptions.AuthenticationFailed('No such user') 

            return (user, None) # authentication successful
            
        else:
            print("bearer_missing")
            return None
