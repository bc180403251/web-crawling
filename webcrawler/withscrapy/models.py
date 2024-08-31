from django.db import models

# Create your models here.

class crawledData(models.Model):
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
