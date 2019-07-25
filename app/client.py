import logging
import multiprocessing
import pathlib
import datetime

from app.pool_workers import calculate_hash


class Client:
    BASE_URL = ''

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
        self.pool: multiprocessing.Pool = multiprocessing.Pool(num_processes)
        self.path: pathlib.Path = pathlib.Path(path)
        self.start_time: datetime.date = datetime.date.fromisoformat(start_time)
        self.end_time: datetime.date = datetime.date.fromisoformat(end_time)
        self.resolution: str = resolution
        self.timeout: int = timeout

    def prepare(self):
        images_list = [f for f in self.path.glob('*.jpg')]

        logging.info('Calculating hash for already existing images')

        with self.pool as pool:
            self.hashes = set(pool.map(calculate_hash, images_list))

        return self

    def run(self):
        return self
