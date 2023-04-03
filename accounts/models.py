from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True, unique=True)
    email = models.CharField(max_length=200, null=True)
    aadhaar_number = models.CharField(
        max_length=12, blank=True, null=True, unique=True)
    pancard_number = models.CharField(
        max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.user)
