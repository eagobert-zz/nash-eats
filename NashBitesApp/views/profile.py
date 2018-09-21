from NashBitesApp.forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from NashBitesApp.models import Profile
from django.shortcuts import render, redirect

# @login_required
# @transaction.atomic
def ProfileView(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, _('Your profile was successfully updated!'))
      return redirect('website:profile', kwargs={})
    else:
      messages.error(request, _('Please correct the error below.'))

  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })






