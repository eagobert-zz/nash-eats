from django.shortcuts import render
from django.contrib.auth.models import User
from NashBitesApp.forms import UserForm, RegistrationForm
from django.contrib.auth import login


def Register(request):
  """ Creates new user and initial profile """

  if request.method == 'POST':
    user = User.objects.create_user(
      username = UserForm(request.POST['username']),
      password = UserForm(request.POST['password']),
    )

    profile = RegistrationForm(data = request.POST)
    
    profile.vendor_id = user

    user.save()
    
    profile.save()

    if user is not None:
      return login(request, user)