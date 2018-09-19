from NashBitesApp.models import Profile
from django import forms


class RegistrationForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['company_name',]
    labels = {
      'company_name': '',
    }
    widgets = {
      'company_name': forms.TextInput(attrs={'placeholder': 'Company Name'})
    }