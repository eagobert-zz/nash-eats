from NashBitesApp.models import Location

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django import forms
import googlemaps
from django.db.models import Max



def HomeView(request):
    """ 
    View manages home dashboard view 
    Methods:  GET, POST
    """
    if request.method == 'GET':
        search_input = request.GET.get('search-input', None)
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'home/home.html'

        if search_input:
            # Get origin: Geocode data from search input
            gm = googlemaps.Client(key=api_key)
            geocode_result = gm.geocode(search_input)[0]
            geocode_result_origin = geocode_result['formatted_address']
            geocode_result_location = geocode_result['geometry']['location']

            # Get destinations: create array of all vendor's most current timestamp location
            query_results = Location.objects.values().order_by('-timestamp')

            seen = list()
            destinations = []

            # Loop over the list of query_results
            for result in query_results:

                # If value of vendor_id is not in empty list
                if result['vendor_id'] not in seen:

                    # append to destinations list
                    destinations.append(result)

                    # then append value of vendor_id to seen list
                    # This results in having only the most current result for each vendor in destinations list
                    seen.append(result['vendor_id'])

                print(destinations)
                
            # Get distance data from Google based on destination and origin

            # make a marker for the 5 closest vendors

            # place marker on map

        context = {
            'api_key': api_key,
            'search_input': search_input,
            'origin': geocode_result_origin,
            'origin_location': geocode_result_location,
            'destinations': destinations,
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
   