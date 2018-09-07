from django.urls import path
from . import views


urlpatterns = [
  path('', views.Welcome, name='Welcome'),
  path('register/', views.Register, name='register'),
  path('vendor/', views.Vendor ,name='VendorView'),
  path('user/', views.User ,name='UserView'),
]