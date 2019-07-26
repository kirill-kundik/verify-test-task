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
    """
    Application client class. All client pipeline is implemented here.
    In init function required named args needs to be passed.
    Then needs to be called prepare() function that will store in set
    (RAM memory) image hashes. And then run() function will start scrapping
    processors and will download all images.
    """
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
        """
        Constructing client. Storing all necessary params
        :param path: path where is images stored and will be stored new wallpapers
        :param num_processes: num of user CPUs
        :param start_time: start time from which wallpapers is needed
        :param end_time: end time from which wallpapers is needed
        :param resolution: needed resolution for wallpapers
        :param timeout: timeout for downloading images requests
        """
        self.hashes = None
        self.num_processes: int = num_processes
        self.path: pathlib.Path = pathlib.Path(path)
        self.start_time: datetime.date = datetime.date.fromisoformat(start_time)
        self.end_time: datetime.date = datetime.date.fromisoformat(end_time)
        self.resolution: str = resolution
        self.timeout: int = timeout

    def prepare(self):
        """
        Preparing app client: read all files from user defined path and
        get all image hashes in set. SHA256 is used, it's speed more than 170Mbps,
        so it's OK even for more than 40-50Gb wallpapers images before downloaded.
        Work in process pool for speed boost
        :return: self
        """
        images_list = [f for f in self.path.glob('*.jpg')]

        logging.info('Calculating hash for already existing images')

        with multiprocessing.Pool(self.num_processes) as pool:
            self.hashes = set(pool.map(self._calculate_hash, images_list))

        return self

    def run(self):
        """
        Starting client and scrapping jobs. And then get results from
        scrapping (url list of images) and start processes in pool for
        downloading and storing non-duplicate images.
        :return: self
        """
        if self.hashes is None:
            logging.error(f'prepare() function was not called before')
            return None
        # results = []
        queue = multiprocessing.Queue()
        pool = [multiprocessing.Process(target=self._queue_worker, args=(queue,)) for _ in range(self.num_processes)]
        for process in pool:
            process.start()
        # pool = multiprocessing.Pool(self.num_processes, self._worker_main, (queue,))

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
            # results.append(item)
            for x in item['urls']:
                queue.put(x)

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
        for _ in range(self.num_processes):
            queue.put('STOP')
        # results = [x for res in results for x in res['urls']]

        # logging.info(f'ALL IMAGES URLS: {", ".join(results)}')

        # with multiprocessing.Pool(self.num_processes) as pool:
        #     pool.map(self._process_urls, results)
        for process in pool:
            process.join()
        return self

    def _queue_worker(self, queue):
        for url in iter(queue.get, 'STOP'):
            logging.info(f'Processing {url}')
            self._process_urls(url)
        logging.info(f'All url processed by this worker')
        return

    def _process_urls(self, image_url):
        """
        Downloading image from image_url, check if it's not already stored
        in directory and store it.
        :param image_url: image url that needs to be downloaded and stored
        :return:
        """
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
        """
        calculating hash for file that already stored on user file system
        :param file_uri: file url on disk
        :return: string hexdigest of sha256
        """
        with open(file_uri, 'rb') as in_file:
            return hashlib.sha256(in_file.read()).hexdigest()
