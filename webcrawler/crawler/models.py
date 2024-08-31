from django.db import models

# Create your models here.

class ScrapedData(models.Model):
    urls = models.URLField(max_length=200)
    title = models.CharField(max_length=255)
    emails=models.EmailField(null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    images = models.JSONField(default=list)  # Storing list of image URLs
    categories = models.CharField(max_length=255, blank=True, null=True)
    row = models.JSONField(null=True) 
