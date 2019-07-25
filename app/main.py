import multiprocessing
import pathlib
import time

from app.utils import parse_args


def process_file(file_uri):
    with open(file_uri, 'rb') as in_file:
        return in_file.read()


if __name__ == '__main__':

    args = parse_args()

    num_processes = max(multiprocessing.cpu_count() - 1, 1)
    start = time.time()
    mylist = [f for f in pathlib.Path('/Users/kyrylo_kundik/Downloads/data').glob('**/*jpg')]

    with multiprocessing.Pool(num_processes) as pool:
        hashes = set(pool.map(process_file, mylist))

        print(len(hashes))
    print(f'Time: {time.time() - start} s')
