from django.urls import path
from .views import crawl_website


urlpatterns = [
    path('', crawl_website, name='crawl_site'),

]
