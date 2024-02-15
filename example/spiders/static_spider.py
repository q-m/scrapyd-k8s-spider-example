import os
import time
from scrapy import Spider

class StaticSpider(Spider):
    name = "static"
    start_urls = ["file:///dev/null"]

    def parse(self, response):
        # allow customizing how long the spider is running at least
        sleep = self.settings.getfloat('STATIC_SLEEP', 0)
        if sleep:
            self.logger.info('Sleeping for ' + str(sleep) + ' seconds')
            time.sleep(sleep)
        # yield a single static item
        yield {
            'text': self.settings.get('STATIC_TEXT', 'To be or not to be'),
            'author': self.settings.get('STATIC_AUTHOR', 'Shakespeare'),
            'tags': os.getenv('STATIC_TAGS', 'static')
        }
