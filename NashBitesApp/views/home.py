from NashBitesApp.models import Location

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django import forms
import googlemaps
from django.db.models import Max
from NashBitesApp.forms import SearchForm



def HomeView(request):
    """ 
    View manages home dashboard view 
    Methods:  GET, POST
    """
    if request.method == 'GET':
        # search_input = request.GET.get('search-input', None)
        search_form = SearchForm()
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'home/home.html'
        # gm = googlemaps.Client(key=api_key)

        # if search_input:
        #     # Get origin: Geocode data from search input
        #     geocode_result = gm.geocode(search_input)[0]
        #     origin = geocode_result['formatted_address']
        #     geocode_result_location = geocode_result['geometry']['location']

        #     # Get destinations: create query_result = list of dictionaries of all vendor's most current timestamp location
        #     query_results = Location.objects.values().order_by('-timestamp')

        #     seen = list()
        #     destinations = []

        #     # Loop over query results
        #     for result in query_results:

        #         # If value of vendor_id is not in empty list
        #         if result['vendor_id'] not in seen:

        #             # append to destinations list
        #             destinations.append(result['address'])

        #             # then append value of vendor_id to seen list that results in having only the most current result for each vendor in destinations list
        #             seen.append(result['vendor_id'])

                
        # # Get distance data from Google based on destination and origin
        # if destinations:
        #    dist_results = gm.distance_matrix(origin, destinations)
        #    print(dist_results)
        # # make a marker for the 5 closest vendors

        #     # place marker on map

        context = {
            'api_key': api_key,
            'search_form': search_form,
            # 'search_input': search_input,
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
   