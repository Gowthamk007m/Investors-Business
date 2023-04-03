from django.db import models

from accounts.models import UserProfile
from business_app.models import Business


# Create your models here.

class User_Query(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Business_name=models.ForeignKey(Business, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user.name)