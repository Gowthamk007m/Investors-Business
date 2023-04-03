from django.db import models

from accounts.models import UserProfile


# Create your models here.




class Banker(models.Model):
    banker = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=100)
    interest_rate = models.FloatField()
    loan_amount = models.FloatField()
    asset_type = models.CharField(max_length=100)
    Description=models.TextField(max_length=600, blank=True, null=True)
