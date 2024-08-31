from django.urls import path
from .views import start_crawling

urlpatterns = [
    path('start-crawling/', start_crawling, name='start_crawling'),
]