from django.contrib import admin
from .models import ScrapedData

# Register your models here.

@admin.register(ScrapedData)
class ScrapdataAdmin(admin.ModelAdmin):
    list_display= ('id', 'urls', 'title')