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
