import scrapy
from scrapy.crawler import CrawlerProcess
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os

class FalloutContentSpider(scrapy.Spider):
    name = "fallout_content"

    def start_requests(self):
        with open('fallout_links.json') as f:
            links = json.load(f)
        for link in links:
            yield scrapy.Request(url=link['link'], callback=self.parse, meta={'category': link['category']})

    def parse(self, response):
        # Extract the title from the URL
        parsed_url = urlparse(response.url)
        title = parsed_url.path.split('/')[-1].replace('_', ' ')
        category = response.meta['category']
        filename = f"scraped_data/{category}_{title}.json"

        html_content = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        content = {}
        sections = soup.find_all('h2')
        
        for section in sections:
            section_header = section.find('span', {'id': True})
            if section_header:
                section_id = section_header['id']
                section_content = []
                for sibling in section.find_next_siblings():
                    if sibling.name in ['h2', 'div']:
                        break
                    text = sibling.get_text(separator=' ', strip=True)
                    if text:
                        section_content.append(text)
                if section_content:
                    content[section_id] = ' '.join(section_content).strip()
        
        if content:
            os.makedirs('scrape_data', exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({'title': title, 'category': category, 'content': content}, f, ensure_ascii=False, indent=4)

process = CrawlerProcess()
process.crawl(FalloutContentSpider)
process.start()
