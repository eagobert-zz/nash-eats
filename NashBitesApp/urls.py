from django.urls import path
from . import views


app_name = "website"

urlpatterns = [
  
  # Django provides a built in url for login:
  # auth/login/ [name='login'] under include('django.contrib.auth.urls')
  # in NashBitesProject urls.py file

  path('', views.Welcome, name='welcome'),
  path('register/', views.Register, name='register'),
  path('home/', views.HomeView.as_view() ,name='home'),
  path('vendor/', views.VendorView.as_view(), name='vendor'),
]