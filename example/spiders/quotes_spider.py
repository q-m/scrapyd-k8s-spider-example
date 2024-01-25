import re
from scrapy import Spider, Request

def unquote(text):
    return re.sub(r'\A“(.*)”\Z', r'\1', text)

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': unquote(quote.css("span.text::text").get()),
                'author': quote.css("small.author::text").get(),
                'tags': quote.css("div.tags > a.tag::text").get()
            }

        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield Request(response.urljoin(next_page_url))
