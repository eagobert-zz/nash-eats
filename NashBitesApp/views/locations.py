from django.shortcuts import render
from django.http import JsonResponse
from NashBitesApp.models import Location


def Location_List(request):
  """ View queries location database table data """
  locations = Location.objects.all().values()
  location_list = list(locations)
  return JsonResponse(location_list, safe=False)