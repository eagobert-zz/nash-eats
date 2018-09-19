from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from NashBitesApp.forms import UserForm

def Login(request):
  if request.method == 'GET':
    login_form = UserForm()
    return render(request, 'registration/login.html', {'login_form': login_form})
  
