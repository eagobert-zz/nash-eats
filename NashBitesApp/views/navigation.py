from django.shortcuts import render
from django.contrib.auth.models import User
from NashBitesApp.forms import SearchForm


def NavView(request):
  if request.method == 'GET':
      template_name = 'navbar.html'
      search_form = SearchForm()
      user = request.user
      context = {
        'user': user,
        'search_form': search_form,
      }
      return render(request, template_name, context)
  