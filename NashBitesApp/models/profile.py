from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
  """ Model represents vendor profile info """
  vendor_id = models.OneToOneField(User, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=50)
  website_url = models.URLField(blank=True)
  twitter_handle = models.CharField(max_length=10, blank=True)
  instagram_handle = models.CharField(max_length=10, blank=True)
  facebook_handle = models.CharField(max_length=10, blank=True)

  class Meta:
    db_table = 'profiles'

  def __str__(self):
    return self.company_name
