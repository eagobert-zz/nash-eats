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
        search_form = SearchForm()
        search_input = request.GET.get('search-input', None)
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'home/home.html'
        context = {
            'api_key': api_key,
            'search_form': search_form,
        }

        if search_input:
            print(search_input)
            # gm = googlemaps.Client(key=api_key)
            # geocode_result = gm.geocode('1600 Amphitheatre Parkway, Mountain View, CA')[0]

        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
   