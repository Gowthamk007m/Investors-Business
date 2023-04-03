from django.db import models

from accounts.models import UserProfile
from user_app.models import User_Query


# Create your models here.
class Advisors(models.Model):
    query = models.ForeignKey(User_Query, on_delete=models.CASCADE)
    advisor_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.advisor_name.name)
