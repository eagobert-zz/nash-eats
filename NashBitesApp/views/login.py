from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from NashBitesApp.forms import UserForm

def Login(request):
  if request.method == 'GET':
    login_form = UserForm()
    return render(request, 'registration/login.html', {'login_form': login_form})

  elif request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/vendor/')

  
