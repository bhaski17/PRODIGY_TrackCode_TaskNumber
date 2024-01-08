scrapy runspider whisky_spider.py
import pandas as pd

# Load JSON file into DataFrame
df = pd.read_json('whisky_data.json')

# Print the DataFrame
print(df)

import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class WhiskySpider(scrapy.Spider):
    name = 'whisky_spider'
    start_urls = ['https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=1&psize=24&sort=pasc']

    def parse(self, response):
        product_links = response.css('li.product-grid__item a.product-card::attr(href)').extract()
        yield from response.follow_all(product_links, self.parse_whisky)

        next_page = response.css('li.pagination-next a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_whisky(self, response):
        name = response.css('h1.product-main__name::text').get()
        price = response.css('p.product-action__price::text').get()
        about = response.css('div.product-main__description::text').get()
        rating = response.css('div.review-overview::text').get()

        yield {
            'name': name,
            'price': price,
            'about': about,
            'rating': rating,
        }

def run_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'whisky_data.json'
    })

    process.crawl(WhiskySpider)
    process.start()

    # Convert JSON to DataFrame
    df = pd.read_json('whisky_data.json')
    print(df)

if __name__ == '__main__':
    run_spider()
