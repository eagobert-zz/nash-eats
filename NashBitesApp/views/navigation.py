from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User


class NavView(View):
    template_name = 'navbar.html'

    def get(self, request, *args, **kwargs):
      user = request.user
      context = {
        'user': user
      }
      return render(request, 'navbar.html', context)
