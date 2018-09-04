from django.contrib.auth.models import User
from django.db import models

class Image(models.Model):
  """ Model represents vendor stored images """
  image = models.ImageField(upload_to='images')
  vendor_id = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'images'

  def __str__(self):
    return self.image