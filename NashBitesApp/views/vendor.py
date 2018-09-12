from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import googlemaps

from NashBitesApp.forms import LocationForm
from NashBitesApp.models import Location


@login_required
def Add_Location(request):
    """ 
    View manages vendor dashboard view 
    Methods:  GET, POST
    """
    if request.method == 'GET':
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        gmaps = googlemaps.Client(key=api_key)
        template_name = 'vendor/vendor.html'
        location_list = Location.objects.all()
        location_form = LocationForm()
        address = location_form['address'].value()
        lat = location_form['latitude'].value()
        long = location_form['longitude'].value()
        context = {
            'location_form': location_form,
            'location_list': location_list,
            'api_key': api_key
        }
        
        # if lat and long is not None:
        #     # reverse geocode to find address
        #     reverse_geocode_result = gmaps.reverse_geocode((lat, long))
        #     # save address to address field

        #     # print results of reverse geocode
        #     print(reverse_geocode_result)

        return render(request, template_name, context)

    elif request.method == 'POST':
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        location_form = LocationForm(data=request.POST)

        if location_form.is_valid():
            location = location_form.save(commit=False)
            location.vendor = request.user
            location.save()
        return HttpResponseRedirect('/vendor/')
