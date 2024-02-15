import os
from scrapy import Spider

class StaticSpider(Spider):
    name = "static"
    start_urls = ["file:///dev/null"]

    def parse(self, response):
        yield {
            'text': self.settings.get('STATIC_TEXT', 'To be or not to be'),
            'author': self.settings.get('STATIC_AUTHOR', 'Shakespeare'),
            'tags': os.getenv('STATIC_TAGS', 'static')
        }
