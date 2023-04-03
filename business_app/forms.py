from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['Business_name','Category','registration_number','Description','Experience','Skills','Active']
        widgets = {
            'Business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Category': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Experience': forms.TextInput(attrs={'class': 'form-control'}),
            'Skills': forms.TextInput(attrs={'class': 'form-control'}),
            'Active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }