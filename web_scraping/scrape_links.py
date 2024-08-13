import scrapy
from scrapy.crawler import CrawlerProcess
import json

class FalloutLinkSpider(scrapy.Spider):
    name = "fallout_links"
    start_urls = ['https://fallout.fandom.com/wiki/Portal:Fallout:_New_Vegas']

    def parse(self, response):
        links_data = []
        for p in response.css('p'):
            category = p.css('a::text').get()
            if category:
                ul = p.xpath('following-sibling::ul[1]')
                for li in ul.css('li'):
                    link = li.css('a::attr(href)').get()
                    if link and link.startswith('/wiki/') and not any(excl in link for excl in [':', '#']):
                        full_link = 'https://fallout.fandom.com' + link
                        links_data.append({'category': category, 'link': full_link})
        
        with open('fallout_links.json', 'w', encoding='utf-8') as f:
            json.dump(links_data, f, ensure_ascii=False, indent=4)

process = CrawlerProcess(settings={
    'FEEDS': {
        'fallout_links.json': {'format': 'json'},
    },
})

process.crawl(FalloutLinkSpider)
process.start()
