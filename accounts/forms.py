from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    aadhaar = forms.CharField(max_length=12)
    pan_card = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=10)
