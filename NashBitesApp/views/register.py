from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from NashBitesApp.forms import UserForm, RegistrationForm


def Register(request):
    ''' Creates a new user and initial profile data '''

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        registration_form = RegistrationForm(data=request.POST)

        if user_form.is_valid():
          
            user = user_form.save()
            profile = registration_form.save(commit=False)
            profile.vendor = user
            profile.save()

            user.set_password(user.password)
            user.save()
            login(request, user)

        return HttpResponseRedirect('/vendor/')

    elif request.method == 'GET': 
        registration_form = RegistrationForm()
        user_form = UserForm()
        context = {
          'user_form': user_form, 
          'registration_form': registration_form
          }

        return render(request, 'registration/register.html', context)
