import datetime

import scrapy
from scrapy.http import Request


class WallpapersSpider(scrapy.Spider):
    name = 'wallpapers'
    start_urls = ['https://www.smashingmagazine.com/category/wallpapers/']

    def __init__(self, start_time, end_time, resolution, **kwargs):
        super().__init__(**kwargs)
        self.start_time: datetime.date = start_time
        self.end_time: datetime.date = end_time
        self.resolution: str = resolution
        self.base_url = 'https://www.smashingmagazine.com'
        self.flag = True

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
