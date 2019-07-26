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
    parser.add_argument('--start-time', '--S',
                        help='Start time for period in which wallpapers published. In yyyy-mm-dd format',
                        type=str,
                        required=True)
    parser.add_argument('--end-time', '--E',
                        help='End time for period in which wallpapers published. In yyyy-mm-dd format',
                        type=str,
                        required=True)
    parser.add_argument('--resolution', '--R',
                        help='Resolution in which wallpapers needs to be downloaded. eg.: 1280x720, 320x480, 2560x1440',
                        type=str,
                        required=True)
    parser.add_argument('--log-file', '--L',
                        help='Path where to store log file, default: output.log',
                        type=str,
                        default='output.log')
    parser.add_argument('--timeout', '--T',
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
    console = logging.StreamHandler()
    if verbose:
        console.setLevel(logging.INFO)
    else:
        console.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

    logging.info('ARGS PARSED, LOGGING CONFIGURED.')


def check_params(args: argparse.Namespace) -> bool:
    """
    check cli parameters for patterns and check for existing directories/files
    :param args: passed args
    :return: true if all correct or false
    """
    path = pathlib.Path(args.path)
    if not path.is_dir():
        logging.error(f'Folder is not exists or it\'s a file : {path}')
        return False

    import re
    r = re.compile(r'^\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$')

    if not r.match(args.start_time):
        logging.error(f'Start time doesn\'t match pattern yyyy-mm-dd: {args.start_time}')
        return False

    if not r.match(args.end_time):
        logging.error(f'End time doesn\'t match pattern yyyy-mm-dd: {args.end_time}')
        return False

    r = re.compile(r'[0-9]{3,4}x[0-9]{3,4}')

    if not r.match(args.resolution):
        logging.error(f'Resolution doesn\'t match pattern 000x0000 or 000x000 or 0000x0000: {args.resolution}')
        return False

    return True


def store_file(content: bytearray, path: pathlib.Path):
    """
    Storing image file
    :param content: bytearray object that will be stored
    :param path: path to the file where to store content
    :return:
    """
    logging.info(f'Storing file into {path}')
    with open(str(path), 'wb') as output:
        output.write(content)
        logging.info(f'Successfully stored into: {path}')


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
