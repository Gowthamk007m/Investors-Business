

from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile
from business_app.models import Business


class InvestorsModel(models.Model):
    User = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE,null=True)
    investment_type = models.CharField(max_length=250)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=100,null=True)
    expected_revenue = models.PositiveIntegerField()
    skill_set = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.User)

