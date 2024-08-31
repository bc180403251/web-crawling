import scrapy
import re

from scrapy.http import Response

from webcrawler_scrapy.items import WebcrawlerScrapyItem


class mySpider(scrapy.Spider):
    
    name='my_spider'
    
    start_urls=[]
    
    def parse(self, response):
        images=response.css('img::attr(src)').getall()
        emails= re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
        locations=re.findall(r'\b(?:[A-Za-z]+\s?){2,5}\b', response.text)
        addresses= re.findall(r'\d{1,5}\s\w+(\s\w+){1,4}', response.text)
        
        yield{
            'url': response.url,
            'image_url':images,
            'email':emails,
            'location':locations,
            'address': addresses
        }
