from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
  """ Model represents vendor location info """
  address = models.CharField(max_length=255)

  latitude = models.DecimalField(
    max_digits=9, 
    decimal_places=6, 
    null=True, 
    blank=True
    )
                
  longitude = models.DecimalField(
    max_digits=9, 
    decimal_places=6, 
    null=True, 
    blank=True
    )

  timestamp = models.DateTimeField(auto_now_add=True)

  vendor_id = models.ManyToManyField(User)


  class Meta:
    db_table = 'locations'

  def __str__(self):
    return self.address