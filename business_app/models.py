from django.db import models

from accounts.models import *

# Create your models here.
class Business(models.Model):
    User = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Business_name=models.CharField(max_length=255, blank=True, null=True)
    Category=models.CharField(max_length=255, blank=True, null=True,)
    registration_number = models.CharField(max_length=255)
    Description=models.CharField(max_length=600, blank=True, null=True)
    Experience=models.CharField(max_length=555, blank=True, null=True)
    Skills=models.CharField(max_length=655, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    Active=models.BooleanField(default=False)


    def __str__(self):
        return str(self.Business_name)