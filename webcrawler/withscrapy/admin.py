from django.contrib import admin
from .models import crawledData
# Register your models here.

@admin.register(crawledData)
class crawladmin(admin.ModelAdmin):
    list_display= ('id', 'url')
