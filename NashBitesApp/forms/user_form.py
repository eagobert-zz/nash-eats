from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
  password = forms.CharField(
    label="", 
    widget=forms.PasswordInput
  )

  class Meta:
    model = User
    fields = ['username', 'password']
    labels = {
      'username': '',
      # 'password': ''
    }
    help_texts = {
      'username': '',
    }
    widgets = {
      'username': forms.TextInput(attrs={'placeholder': 'Username'})
    }