from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import *
from django.db.models import Q


User = get_user_model()

class AadhaarOrPANCardBackend(ModelBackend):
    def authenticate(self, request, identifier=None, password=None, **kwargs):
        try:
            user_profile = UserProfile.objects.get(Q(aadhaar_number=identifier)|Q(pancard_number=identifier))
            user = user_profile.user
            if user.check_password(password):
                return user
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


