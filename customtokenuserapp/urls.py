from django.urls import path, include
from customtokenuserapp.views import CustomUserToken


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'customusertoken', CustomUserToken, basename='CustomUserToken'),



urlpatterns = [
    path('', include(router.urls)),

]