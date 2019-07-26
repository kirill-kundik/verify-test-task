import datetime
import hashlib
import logging
import multiprocessing
import pathlib

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from app.crawler import WallpapersSpider
from app.utils import download_file, store_file


class Client:
    BASE_URL = 'https://www.smashingmagazine.com/category/wallpapers/'

    def __init__(
            self,
            *,
            path: str,
            num_processes: int,
            start_time: str,
            end_time: str,
            resolution: str,
            timeout: int
    ):
        self.hashes = None
        self.num_processes: int = num_processes
        self.path: pathlib.Path = pathlib.Path(path)
        self.start_time: datetime.date = datetime.date.fromisoformat(start_time)
        self.end_time: datetime.date = datetime.date.fromisoformat(end_time)
        self.resolution: str = resolution
        self.timeout: int = timeout

    def prepare(self):
        images_list = [f for f in self.path.glob('*.jpg')]

        logging.info('Calculating hash for already existing images')

        with multiprocessing.Pool(self.num_processes) as pool:
            self.hashes = set(pool.map(self._calculate_hash, images_list))

        return self

    def run(self):
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_passed)
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(
            WallpapersSpider,
            start_time=self.start_time,
            end_time=self.end_time,
            resolution=self.resolution,
            start_url=self.BASE_URL
        )
        logging.getLogger('scrapy').setLevel(logging.ERROR)
        process.start()

        results = [x for res in results for x in res['urls']]

        logging.info(f'ALL IMAGES URLS: {", ".join(results)}')

        with multiprocessing.Pool(self.num_processes) as pool:
            pool.map(self._process_urls, results)

        return self

    def _process_urls(self, image_url):
        image_name = pathlib.Path(image_url).name
        image = download_file(image_url, self.timeout)
        if image is not None:
            if not hashlib.sha256(image).hexdigest() in self.hashes:
                store_file(image, self.path / image_name)
            else:
                logging.info(f'File has been downloaded previous time. Skipping... Image name: {image_name}')
        else:
            logging.warning(f'Got None instead of image content from: {image_url}')

    @staticmethod
    def _calculate_hash(file_uri):
        with open(file_uri, 'rb') as in_file:
            return hashlib.sha256(in_file.read()).hexdigest()
