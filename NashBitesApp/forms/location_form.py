from NashBitesApp.models import Location
from django import forms
# from django.conf import settings


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'address',
            'latitude',
            'longitude'
        ]
        labels = {
            'address': '',
            'latitude': '',
            'longitude': '',
        }
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter an address. . .'}),
            'latitude': forms.NumberInput(attrs={'placeholder': 'Auto generated latitude. . .'}),
            'longitude': forms.NumberInput(attrs={'placeholder': 'Auto generated longitude. . .'}),
        }
