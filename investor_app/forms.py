from .models import *
from django import forms


class InvestorsForm(forms.ModelForm):
    class Meta:
        model = InvestorsModel
        exclude = ['User', 'business']


