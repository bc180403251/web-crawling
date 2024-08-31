# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerScrapyItem(scrapy.Item):
    url = scrapy.Field()
    image_url = scrapy.Field()
    email = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
