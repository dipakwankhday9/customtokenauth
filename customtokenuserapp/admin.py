from django.contrib import admin
from customtokenuserapp.models import CustomToken, CustomUser

# Register your models here.
admin.site.register(CustomToken)
admin.site.register(CustomUser)