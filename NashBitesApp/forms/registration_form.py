from NashBitesApp.models import Profile
from django import forms


class RegistrationForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['company_name',]