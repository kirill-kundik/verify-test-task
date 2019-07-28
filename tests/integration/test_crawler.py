from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from app.crawler import WallpapersSpider


def test_parser_true(start_time, end_time, resolution, start_url, correct_res):
    res = []

    def crawler_results(signal, sender, item, response, spider):
        """
        help function for getting result when one page scrapped
        :param signal:
        :param sender:
        :param item:
        :param response:
        :param spider:
        :return:
        """
        for x in item['urls']:
            res.append(x)

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(
        WallpapersSpider,
        start_time=start_time,
        end_time=end_time,
        resolution=resolution,
        start_url=start_url
    )
    process.start()

    assert sorted(correct_res) == sorted(res)
