from NashBitesApp.models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'company_name', 
      'website_url', 
      'twitter_handle', 
      'instagram_handle', 
      'facebook_handle'
      ]