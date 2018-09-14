from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django import forms
import googlemaps
from NashBitesApp.forms import SearchForm


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
            print(search_input)
            gm = googlemaps.Client(key=api_key)
            geocode_result = gm.geocode(search_input)[0]
            geocode_result_origin = geocode_result['formatted_address']
            geocode_result_location = geocode_result['geometry']['location']

        context = {
            'api_key': api_key,
            'search_input': search_input,
            'origin': geocode_result_origin,
            'origin_location': geocode_result_location,
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
   