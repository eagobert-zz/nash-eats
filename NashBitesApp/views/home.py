from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import googlemaps


def HomeView(request):
    if request.method == 'GET':
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'home/home.html'
        context = {
            'api_key': api_key,
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        return HttpResponseRedirect()
   