from .models import *
from django import forms


class BankerForm(forms.ModelForm):
    class Meta:
        model = Banker
        fields = [ 'loan_type', 'interest_rate', 'loan_amount', 'asset_type','Description']
        
