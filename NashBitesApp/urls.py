from django.urls import path
from django.conf.urls import url
from . import views


app_name = "website"

urlpatterns = [
  
  # Django provides a built in url for login:
  # auth/login/ [name='login'] under include('django.contrib.auth.urls')
  # in NashBitesProject urls.py file

  path('', views.Welcome, name='welcome'),
  path('register/', views.Register, name='register'),
  path('home/', views.HomeView ,name='home'),
  path('vendor/', views.VendorView, name='vendor'),
  path('location/', views.Location_List, name='locations'),
  # path('login/', views.Login, name='login'),
  url(r'^profile/(?P<username>[\w.@+-]+)/$', views.ProfileView, name='profile'),
]