import argparse
import logging
import pathlib

import requests


def parse_args():
    """
    Program argument parsing
    :return: all parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='CLI program for auto downloading wallpapers.'
    )
    parser.add_argument('--path', '--P',
                        help='Path to the folder where to store images and where previous images exist (preferably).',
                        type=str,
                        required=True)
    parser.add_argument('--log-file', '--L',
                        help='Path where to store log file, default: output.log',
                        type=str,
                        default='output.log')
    parser.add_argument('--tiemout', '--T',
                        help='Timeout for each request out of the program in seconds, default 10s',
                        type=int,
                        default='10')
    parser.add_argument('--verbose', '--V',
                        help='Printing whole program log to the console.',
                        action='store_true')
    return parser.parse_args()


def setup_logging(log_file: pathlib.Path, verbose: bool):
    """
    Set up program logging
    :param log_file: file where to store log
    :param verbose: if needed printing whole log into console
    :return: None
    """
    logging.root.handlers = []
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        filename=log_file,
                        filemode='a')
    if verbose:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)

    logging.info('ARGS PARSED, LOGGING CONFIGURED.')


def store_file(content: bytearray, path: pathlib.Path):
    """
    Storing image file
    :param content: bytearray object that will be stored
    :param path: path to the file where to store content
    :return:
    """
    with open(str(path), 'wb') as output:
        output.write(content)


def download_file(url: str, timeout: int) -> bytearray:
    """
    Downloading file by url and saving it in path
    :param timeout: timeout for downloading file in seconds
    :param url: file url
    :return: bytearray if downloaded successfully or None
    """
    logging.info(f'Downloading file from {url}')
    try:
        r = requests.get(url=url, timeout=timeout)
        if r.status_code == 200:
            logging.info(f'File from {url} successfully downloaded.')
            return r.content
        else:
            logging.warning(f'Status code of request is not 200 OK. URL: {url}')
    except requests.exceptions.Timeout:
        logging.error(f'HTTP TIMEOUT ERROR. URL: {url}')
    except requests.RequestException as e:
        logging.error(f'EXCEPTION {str(e)}. URL: {url}')
