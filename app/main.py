import logging
import multiprocessing
import time

from app.client import Client
from app.utils import parse_args, check_params, setup_logging

if __name__ == '__main__':
    args = parse_args()

    start = time.time()

    if not check_params(args):
        logging.error(f'Program params wasn\'t correct!')
        exit(1)

    setup_logging(args.log_file, args.verbose)

    num_processes = max(multiprocessing.cpu_count() - 1, 1)

    client = Client(
        path=args.path,
        num_processes=num_processes,
        start_time=args.start_time,
        end_time=args.end_time,
        resolution=args.resolution,
        timeout=args.timeout
    ).prepare()

    logging.info(f'Program execution time: {time.time() - start} s')
