# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from withscrapy.models import crawledData


class WebcrawlerScrapyPipeline:
    def process_item(self, item, spider):
        crawledData.objects.create(
            url=item['url'],
            
            image_url=item.get('image_url'),
            
            email= item.get('email'),
            
            location= item.get('location'),
            
            address= item.get('address')
        )
        
        return item
