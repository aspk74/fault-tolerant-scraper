import scrapy

class ScrapedItem(scrapy.Item):
    url = scrapy.Field()
    data = scrapy.Field()
    timestamp = scrapy.Field()