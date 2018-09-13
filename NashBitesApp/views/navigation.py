from django.shortcuts import render
from django.contrib.auth.models import User


def NavView(request):
  if request.method == 'GET':
      template_name = 'navbar.html'
      user = request.user
      context = {
        'user': user,
      }
      return render(request, template_name, context)
