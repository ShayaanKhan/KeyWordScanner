import csv
from scrapy.crawler import CrawlerProcess
from keyword_crawler.spiders.domain_crawler import DomainCrawlerSpider
import logging

keywords = ["while"]
output_csv_file = "keyword_matches.csv"
batch_size = 5  # Number of domains to process in each batch


def process_batch(domains):
    process = CrawlerProcess(
        settings={
            "FEED_FORMAT": "csv",
            "FEED_URI": output_csv_file,
            "LOG_ENABLED": False,
            "LOG_LEVEL": logging.ERROR,
        }
    )

    for domain in domains:
        process.crawl(DomainCrawlerSpider, domain=domain, keywords=keywords)

    process.start()


def main():
    with open("top10milliondomains.csv", "r") as domain_file:
        domain_reader = csv.DictReader(domain_file)
        domains = [row["Domain"] for row in domain_reader]

    for i in range(0, len(domains), batch_size):
        batch = domains[i : i + batch_size]
        print(f"Processing batch {i // batch_size + 1}")
        process_batch(batch)

    print("Crawling completed. Keyword matches saved to", output_csv_file)


if __name__ == "__main__":
    main()
