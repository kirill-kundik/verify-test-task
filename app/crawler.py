import datetime
from urllib.parse import urlparse

import scrapy
from scrapy.http import Request


class WallpapersSpider(scrapy.Spider):
    """
    Class for scrapping.
    """
    name = 'wallpapers'

    def __init__(self, start_time, end_time, resolution, start_url, **kwargs):
        super().__init__(**kwargs)
        self.start_time: datetime.date = start_time
        self.end_time: datetime.date = end_time
        self.resolution: str = resolution

        self.flag = True
        self.start_urls = [start_url]

        parsed_uri = urlparse(start_url)
        result = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        self.base_url = result

    def parse(self, response):
        res = response.xpath('//p/time')

        for r in res:
            date = datetime.date.fromisoformat(r.xpath('@datetime').get())
            if self.start_time <= date <= self.end_time:
                url = r.xpath('../a/@href').get()
                if url is not None:
                    yield Request(self.base_url + url, callback=self.parse_article)
            elif date < self.start_time:
                self.flag = False

        next_page = response.css('li.pagination__next a::attr("href")').get()
        if next_page is not None and self.flag:
            yield Request(self.base_url + next_page, callback=self.parse)

    def parse_article(self, response):
        r = response.xpath(f'//ul/li/a[text()[re:test(., "^{self.resolution}$")]]/@href').getall()
        yield {
            'urls': r
        }
