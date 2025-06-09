import scrapy
from scrapy.exceptions import CloseSpider
from scraper.items import ScrapedItem

class RobustSpider(scrapy.Spider):
    name = "robust"
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 4,
        'DOWNLOAD_DELAY': 2,
    }

    def start_requests(self):
        urls = [
            'https://example.com/page1',
            'https://example.com/page2'
        ]
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                errback=self.handle_error,
                meta={'retry_count': 0}
            )

    def parse(self, response):
        if response.status == 200:
            yield ScrapedItem(
                url=response.url,
                data=response.css('p::text').getall()
            )
        else:
            self.logger.error(f"Failed on {response.url}")

    def handle_error(self, failure):
        retry_count = failure.request.meta.get('retry_count', 0)
        if retry_count < self.custom_settings['RETRY_TIMES']:
            self.logger.warning(f"Retrying {failure.request.url}")
            return failure.request.copy_with(
                meta={'retry_count': retry_count + 1}
            )
        else:
            self.logger.error(f"Permanently failed {failure.request.url}")