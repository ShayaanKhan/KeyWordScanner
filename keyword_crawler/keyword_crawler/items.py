import scrapy

class KeywordCrawlerItem(scrapy.Item):
    url = scrapy.Field()
    keywords = scrapy.Field()
