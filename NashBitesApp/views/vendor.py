from NashBitesApp.forms import LocationForm
from NashBitesApp.models import Location
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings



def Add_Location(request):
    """ View manages the GET, POST methods of the vendor page view """
    if request.method == 'GET':
        api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
        template_name = 'vendor/vendor.html'
        location_list = Location.objects.all()
        location_form = LocationForm()
        context = {
            'location_form': location_form,
            'location_list': location_list,
            'api_key': api_key
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        location_form = LocationForm(data=request.POST)

        if location_form.is_valid():
          
            location = location_form.save(commit=False)
            location.vendor = request.user
            location.save()

        return HttpResponseRedirect('/vendor/')
