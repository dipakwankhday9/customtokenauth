import binascii
import os
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    token = models.CharField(max_length=500)
    
    
    def __str__(self) -> str:
        return self.username
    
    def is_authenticated(self):
        return True


class CustomToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    
    customuser = models.OneToOneField(CustomUser, related_name='auth_token',on_delete=models.CASCADE, verbose_name="CustomUser")
    created =models.DateTimeField(_("Created"), auto_now_add=True)
    
    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")
        
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(CustomToken, self).save(*args, **kwargs)
    
    def generage_key(self):
        return binascii.hexlify(os.urandom(20)).decode()
    
    def __str__(self):
        return self.key
    

        
    #binascii : Convert between binary and ASCII
    #OS: OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality.