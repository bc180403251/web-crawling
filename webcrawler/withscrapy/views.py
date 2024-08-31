# crawler/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import URLForm
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webcrawler_scrapy.spiders.my_spider import mySpider

def start_crawling(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # Configure Scrapy process
            settings = get_project_settings()
            process = CrawlerProcess(settings)
            # Start the spider with the user-provided URL
            process.crawl(mySpider, start_urls=[url])
            process.start()
            return HttpResponse("Crawling started.")
    else:
        form = URLForm()
    return render(request, 'crawlers\crawlerForm.html', {'form': form})
