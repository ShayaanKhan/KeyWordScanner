import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from keyword_crawler.items import KeywordCrawlerItem

class DomainCrawlerSpider(CrawlSpider):
    name = "domain_crawler"

    allowed_domains = []  # Domains will be populated from CSV
    start_urls = []  # URLs will be populated from CSV

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(DomainCrawlerSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [kwargs.get("domain")]
        self.start_urls = [f"https://{kwargs.get('domain')}"]

    def parse_item(self, response):
        item = KeywordCrawlerItem()
        item["url"] = response.url
        item["keywords"] = []

        print(f"Crawler {self.name} is scanning: {response.url}")

        for keyword in self.keywords:
            if keyword.lower() in response.text.lower():
                item["keywords"].append(keyword)

        if item["keywords"]:
            return item  # Only yield items with keywords

        return None  # Discard items without keywords
