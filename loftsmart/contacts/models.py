from django.db import models

class Contactlist(models.Model):
  """This class represents the contactlist model."""
  name = models.CharField(max_length=255, blank=False, unique=True)
  phone = models.CharField(max_length=20, blank=False)
  country = models.CharField(max_length=2, blank=False)
  image = models.CharField(max_length=255, blank=False)
  cleanPhone = models.CharField(max_length=20, blank=False)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
      """Return a human readable representation of the model instance."""
      return "{}".format(self.name)
