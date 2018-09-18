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
        # search_input = request.GET.get('search-input', None)
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'home/home.html'

        context = {
            'api_key': api_key,
            # 'search_input': search_input,
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
   