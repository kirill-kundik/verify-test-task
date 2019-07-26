import datetime
from urllib.parse import urlparse

import scrapy
from scrapy.http import Request


class WallpapersSpider(scrapy.Spider):
    """
    Class for scrapping. As a constructor params it needs start time, end time,
    resolution for which articles needed to be scrapped. Name of scrapper is 'wallpapers'
    """
    name = 'wallpapers'

    def __init__(self, start_time, end_time, resolution, start_url, **kwargs):
        """
        Scrapper constructor. Passed need params for scrapping and calculates base url for parsing
        :param start_time: Start time of articles that will be scrapped
        :param end_time: End time of articles that will be scrapped
        :param resolution: Resolution of images that needs to be downloaded
        :param start_url: Start url from where scrapping will begin
        :param kwargs: super params
        """
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
        """
        Parsing articles pages: get urls for every article and then will parse_article,
        or stop if none of the available pages are present
        :param response: scrapper page response
        :return: yield parsing response as request type or stop scrapping
        """
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
        """
        Parsing one article and get url for passed resolution images
        :param response: scrapper page response
        :return: yield dict with scrapped images urls
        """
        r = response.xpath(f'//ul/li/a[text()[re:test(., "^{self.resolution}$")]]/@href').getall()
        yield {
            'urls': r
        }
